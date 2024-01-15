## Problem Summary
A function portal site made with Python and Django libary for activation of clients for internet access had an upgrade to add in compensation for a day to all clients with downtime.
Clients sent mails to complain and later on calls from clients came through... Over one hundred mails were received with clients complaining to be completly shut out from the portal and those already activated lost access to the internet.
We cloned our site's repository from GitBug, followed the installation instructions on the README and to our surprise the site couldn't startup. It wasn't long before we realized that the cause of the problem was failing to update the requirements for our project.  
The site was malfunctioning from 8:00 PM GMT+1 to 11:20 AM GMT+1.

### Root Cause And Resolution
- 13-01-2023 8:00 AM GMT+1 - Several emails were read regarding different issues our clients faced.
- 13-01-2023 8:32 AM GMT+1 - A dummy payment was made using test accounts by the backend engineer and confirmed no access to the internet.
- 13-01-2023 9:30 AM GMT+1 - Confirmation by general office that no client could log in
- 13-01-2023 10:30 AM GMT+1 - We were misled by thinking that our controllers might be creating a different hash for a valid password of the site's admin.
- 13-01-2023 11:15 AM GMT+1 -  The incident was resolved by updating the requirements (the bcrypt gem version) for the backend server.
- 13-01-2023 11:15 AM GMT+1 - It was also discovered essential parts of the code was deleted during the upgrade to allow for compensation making payment have no effect on the portal.


### Corrective And Preventative Measures
- Setup a continuous integration pipeline to run a build on each pull request branch. This would ensure that builds are passing in the pull request branch before it is merged with the deployment branch.
- Setup a monitoring system for the database and application servers to keep track of any issue that may occur.
- Use of new branch for every update made to reduce the risk of deleted code
- Develop tests that need to be passed for each new feature and those tests should be passing before they are merged with the deployment branch.
