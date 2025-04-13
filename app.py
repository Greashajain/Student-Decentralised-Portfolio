from flask import Flask, request, jsonify
from dotenv import load_dotenv
from web3 import Web3
import json
import os
import requests

load_dotenv()

app = Flask(__name__)

# Load environment variables
INFURA_URL = os.getenv("INFURA_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
PUBLIC_ADDRESS = os.getenv("PUBLIC_ADDRESS")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
PINATA_API_KEY = os.getenv("PINATA_API_KEY")
PINATA_SECRET_API_KEY = os.getenv("PINATA_SECRET_API_KEY")

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(INFURA_URL))
CHAIN_ID = 11155111  # Sepolia

# Load contract ABI
with open("build/contracts/StudentPortfolio.json") as f:
    contract_json = json.load(f)
    contract_abi = contract_json['abi']

# Connect to deployed contract
contract = w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=contract_abi)


# ✅ Upload file to IPFS using Pinata
def upload_to_ipfs(file):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_API_KEY
    }
    response = requests.post(url, files={"file": file}, headers=headers)
    ipfs_hash = response.json()["IpfsHash"]
    return ipfs_hash


# ✅ Create portfolio
@app.route("/create_portfolio", methods=["POST"])
def create_portfolio():
    name = request.json["name"]

    nonce = w3.eth.get_transaction_count(PUBLIC_ADDRESS)
    txn = contract.functions.createPortfolio(name).build_transaction({
        'chainId': CHAIN_ID,
        'from': PUBLIC_ADDRESS,
        'nonce': nonce,
        'gas': 3000000,
        'gasPrice': w3.to_wei("10", "gwei")
    })

    signed_txn = w3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return jsonify({"tx_hash": tx_hash.hex()})


# ✅ Add achievements, projects, activities, certificates
@app.route("/add_data", methods=["POST"])
def add_data():
    data_type = request.json["type"]  # achievements, projects, etc.
    values = request.json["values"]

    func_map = {
        "achievements": contract.functions.addAchievements,
        "projects": contract.functions.addProjects,
        "activities": contract.functions.addExtracurricularActivities,
        "certificates": contract.functions.addCertificates
    }

    if data_type not in func_map:
        return jsonify({"error": "Invalid type"}), 400

    nonce = w3.eth.get_transaction_count(PUBLIC_ADDRESS)
    txn = func_map[data_type](values).build_transaction({
        'chainId': CHAIN_ID,
        'from': PUBLIC_ADDRESS,
        'nonce': nonce,
        'gas': 3000000,
        'gasPrice': w3.to_wei("10", "gwei")
    })

    signed_txn = w3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return jsonify({"tx_hash": tx_hash.hex()})


# ✅ View portfolio
@app.route("/view_portfolio", methods=["GET"])
def view_portfolio():
    user = request.args.get("address").strip()
    user = Web3.to_checksum_address(user) 
    name, achievements, projects, activities, certificates = contract.functions.viewPortfolio(user).call()
    return jsonify({
        "name": name,
        "academicAchievements": achievements,
        "projects": projects,
        "extracurricularActivities": activities,
        "certificates": certificates
    })


# ✅ Upload certificate image to IPFS
@app.route("/upload_certificate", methods=["POST"])
def upload_certificate():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files["file"]
    ipfs_hash = upload_to_ipfs(file)
    return jsonify({"ipfs_hash": ipfs_hash})


if __name__ == "__main__":
    app.run(debug=True)
