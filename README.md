

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

## 📁 Project Structure


## ⚙️ Deployment

1. Setup `.env` file with your private key:
    ```
    PRIVATE_KEY=your_private_key
    ```

2. Deploy on Sepolia Testnet:
    ```bash
    brownie run scripts/deploy.py --network sepolia
    ```

## 🔍 View Portfolio

Use the `viewPortfolio(address)` function to retrieve:
- Name
- Achievements
- Projects
- Extracurriculars
- Certificate IPFS hashes

## 🧪 To Do Next

- [ ] Flask UI for user interaction
- [ ] Upload certificates to IPFS via API
- [ ] Connect Metamask to frontend
- [ ] Add AI-based analysis for student portfolios






![Image](https://github.com/user-attachments/assets/d40635d9-c2aa-4844-b79a-ea6a7d7d9f89)
