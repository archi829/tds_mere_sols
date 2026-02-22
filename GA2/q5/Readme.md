Q5 Solution: Static JSON API
Objective
Host a static JSON API for the StaticShop product catalog on GitHub Pages.

Steps Taken
Data Creation:

Created products.json containing:
Metadata with email (23f3001889@ds.study.iitm.ac.in) and version (a351c038).
List of 18 products with specific details.
Aggregations for the home category (count: 3, inventoryValue: 93782.70).
Repository Setup:

Initialized a new Git repository in ga2/q5.
Added the remote: .
Deployment:

Committed products.json.
Pushed to the main branch of the remote repository.
GitHub Pages Configuration (Manual Step):

Go to Repository Settings -> Pages.
Select Source: Deploy from a branch.
Select Branch: main, Folder: / (root).
Save.
Verify the URL: 