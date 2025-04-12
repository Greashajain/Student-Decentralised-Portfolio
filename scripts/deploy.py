from brownie import StudentPortfolio, accounts
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def main():
    # Access the private key from .env file
    private_key = os.getenv("PRIVATE_KEY")
    
    # Load the account using the private key
    account = accounts.add(private_key)
    
    # Deploy the contract
    print("Deploying StudentPortfolio contract...")
    contract = StudentPortfolio.deploy({'from': account})
    
    print(f"Contract deployed at address: {contract.address}")

    # Example usage of the review function
    # Replace with an actual address (the one that created a portfolio)
    user_address = "0x96a9b0d315387063a2c2E82a47C8aFB486893b65"
    
    # Call viewPortfolio function
    name, achievements, projects, activities, certificates = contract.viewPortfolio(user_address)
    
    print(f"Portfolio of {name}:")
    print(f"Achievements: {achievements}")
    print(f"Projects: {projects}")
    print(f"Extracurricular Activities: {activities}")
    print(f"Certificates: {certificates}")
    
    return contract