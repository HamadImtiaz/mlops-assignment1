# CI/CD Pipeline for Model and Dataset Project

## Description
This repository contains a CI/CD pipeline setup for a project that involves a machine learning model and a unique dataset per group. The pipeline utilizes various tools and technologies including GitHub, GitHub Actions, Jenkins, Docker, Python, Flask, and Git to automate the development, testing, and deployment processes.

## Features
- **Automatic Code Quality Check:** GitHub Actions workflow checks the quality of the code using the flake8 package, ensuring code consistency and adherence to coding standards.
- **Branch Management:** Changes are made to the dev branch only, ensuring a clean and organized development environment.
- **Feature Branches:** When a specific feature is completed and pushed to the remote dev branch, a pull request is made to merge the new feature to the test branch. This triggers another GitHub Actions workflow to perform unit testing, ensuring the stability of the newly added feature.
- **Merging to Master:** Once automated testing is successful, a pull request is made to merge changes to the master branch. This action also triggers a Jenkins job to containerize the application and push it to the Docker Hub.
- **Notification:** Upon successful execution of the Jenkins job and merge to the master branch, an email notification is sent to the administrator.

## Usage
1. Clone the repository to your local machine.
2. Make changes to the dev branch for development purposes.
3. Create feature branches for specific features and push them to the dev branch.
4. When a feature is completed, create a pull request to merge it to the test branch.
5. GitHub Actions will automatically run unit tests on the test branch.
6. If tests are successful, create a pull request to merge changes to the master branch.
7. Jenkins job will be triggered to containerize the application and push it to Docker Hub.
8. Administrator will receive an email notification upon successful execution of the Jenkins job.
