// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentPortfolio {
    struct Portfolio {
        string name;
        string[] academicAchievements;
        string[] projects;
        string[] extracurricularActivities;
        string[] certificates;
    }

    mapping(address => Portfolio) public portfolios;

    function createPortfolio(string memory _name) public {
        portfolios[msg.sender].name = _name;
    }

    function addAchievements(string[] memory achievements) public {
        for (uint i = 0; i < achievements.length; i++) {
            portfolios[msg.sender].academicAchievements.push(achievements[i]);
        }
    }

    function addProjects(string[] memory projects) public {
        for (uint i = 0; i < projects.length; i++) {
            portfolios[msg.sender].projects.push(projects[i]);
        }
    }

    function addExtracurricularActivities(string[] memory activities) public {
        for (uint i = 0; i < activities.length; i++) {
            portfolios[msg.sender].extracurricularActivities.push(activities[i]);
        }
    }

    function addCertificates(string[] memory certificateHashes) public {
        for (uint i = 0; i < certificateHashes.length; i++) {
            portfolios[msg.sender].certificates.push(certificateHashes[i]);
        }
    }

    // ✅ Unified function to return all details of a portfolio
    function viewPortfolio(address user) 
        public 
        view 
        returns (
            string memory name,
            string[] memory achievements,
            string[] memory projects,
            string[] memory activities,
            string[] memory certificates
        ) 
    {
        Portfolio storage p = portfolios[user];
        return (
            p.name,
            p.academicAchievements,
            p.projects,
            p.extracurricularActivities,
            p.certificates
        );
    }
}
