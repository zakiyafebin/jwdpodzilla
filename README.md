# podzilla

### Git and GitHub activity - Forking and pull request
- Login to your GitHub account
- Access Julie’s repository from the link below
   https://github.com/JulieToke/jwdpodzilla
- Fork their repository on GitHub. Use the  button - top right
- In your Terminal, create a new folder in Documents called gen7
    ``` mkdir Documents/gen7 ```
- Move into the folder 
    ``` cd gen7``` 
- From the terminal , clone the forked repository from GitHub within the folder
    ```  git clone https://github.com/{yourusername}/jwdpodzilla ``` 
- Navigate into the cloned directory
  ``` cd jwdpodzilla``` 
- List the contents of the directory
    ```  ls -al``` 
- Add your image file in the images directory in Finder/Folder explorer
- From the terminal, create a new file in your directory and name it yournameprofile.html
  ``` touch yournameprofile.html``` 
- Edit the file yournameprofile.html in VSCode and save the file (Edit your image, image alt, name and role) - see file code at the end of the page
```
<!DOCTYPE html>
<html lang="en">
 <head>
   <meta charset="UTF-8" />
   <meta http-equiv="X-UA-Compatible" content="IE=edge" />
   <meta name="viewport" content="width=device-width, initial-scale=1.0" />
   <link href="css/styles.css" rel="stylesheet" />
   <title>Podzilla - Profiles</title>
 </head>
 <body>
   <div class="card">
     <img src="./images/Julie_2.jpg" alt="Julie" style="width: 100%" />
     <h1>Julie</h1>
     <p class="role">Student, JWD07 - Podzilla</p>
     <p>Generation, Australia</p>
     <p><a href="index.html"><< Home</a></p>
   </div>
 </body>
</html>
```

- Check the status of the directory
     ``` git status``` 
- Add the new file to the staging area
     ```  git add .``` 
- Commit the changes 
    ``` git commit -m "Editing my profile details"``` 
    ``` git log ``` 
- You will see the SHA and log message for the latest commit
- Push the file into the forked Github main repo
    ```  git push``` 
- Go to GitHub and create a pull request on Julie’s repo
- Julie will review your pull request and merge your files to her main repo
