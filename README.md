

# 🎓 Student Decentralized Portfolio System

A blockchain-based platform that allows students to securely store, update, and share their academic achievements, projects, extracurricular activities, and certificates. Uses **Ethereum (Sepolia Testnet)** and **IPFS** for storage, and can be integrated with **AI** for insights.

## 🚀 Features

- ✅ Immutable student portfolios stored on Ethereum.
- 📄 Certificates uploaded by user → Stored on IPFS as hashes.
- 🔍 View full portfolio anytime using `viewPortfolio` function.
- 🔐 Only the student (wallet owner) can modify their own portfolio.
- 🧠 (Planned) AI insights for career or academic growth using Python.

## 💡 Tech Stack

- **Solidity** – Smart contract
- **Brownie** – Deployment & testing
- **IPFS** – Certificate storage
- **Python (Flask)** – Backend integration
- **Metamask** – Wallet interaction
- **HTML CSS Javascript** – Frontend




## ⚙️ Deployment

1. Setup `.env` file with your private key:
    ```
    PRIVATE_KEY=your_private_key
    ```

2. Deploy on Sepolia Testnet:
    ```bash
    brownie run scripts/deploy.py --network sepolia
    ```

## 🔍 How to View Portfolio
Use the viewPortfolio(address) function (via Web3 or frontend button) to retrieve:

👤 Name

🎓 Academic Achievements

💻 Projects

🏆 Extracurricular Activities

📄 IPFS certificate links





## Screenshots


<img src="https://github.com/user-attachments/assets/d40635d9-c2aa-4844-b79a-ea6a7d7d9f89" width="700" />

<div style="display: flex; justify-content: space-around;">
    <img src="https://github.com/user-attachments/assets/5fa8bdb7-557b-4892-ae4d-0b4ab4e67bdd" width="700" />
     <img src="https://github.com/user-attachments/assets/7b1ffd1d-4774-4bdc-afe1-c5fab485ef66" width="600" />
    <img src="https://github.com/user-attachments/assets/109170af-54c9-4c63-86fb-e0eaa9c830bf" width="400" />
    <img src="https://github.com/user-attachments/assets/aa171c78-b906-4523-af7f-0d1a220a1e60" width="300" />
    
   
    
</div>

## 🧪 To Do Next
- [ ] Add AI-based analysis for student portfolios


