# SVG REST API
This application provides REST access to common SVG elements and their attributes.
## Installation 

Clone repository with ``` git clone https://github.com/mkuegeler/svgapi.git ```, go to directory '**svgapi**' ```cd svgapi``` and start it with (Powerhell required):

```app.ps1 up ```

Note: If the powershell script drops a permission error, just use the plain docker-compose command to start the application.
```docker-compose up -d```

Call the script ```app.ps1``` with sequence 'down, clean, up' to refresh changes.
Example: ```app.ps1 down  app.ps1 clean app.ps1 up``` 

## Get updates from repository

 - Go to directory '**svgapi**' ```cd svgapi```
 - Shutdown and remove docker containers: ```app.ps1 down```
 - Remove images: ```app.ps1 clean``` 
 - Run: ```git push origin master```
 - Rebuild application: ```app.ps1 up```

## Run Application
Open ```http://localhost``` in your browser.
