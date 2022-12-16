# Note
In this repository there is the CRUD of an agenda for assigning appointments to the affiliates of a laboratory, this is the version made in Django because it is made in springboot with the name app_laboratory


# ***laboratory_backend***
  This project present through API REST services, the ability to control a laboratory appointment schedule.  
  A CRUD was implemented for this purpose.
  
  ### Distribution of the tables
![image](https://user-images.githubusercontent.com/81341089/205459243-f827dc83-cfbb-4451-bd80-de46482c7739.png)

 
   #### laboratory/apiView:
        contains all the views and business logic.

   #### laboratory/models:
        contains the models of the tables in the database
    
   #### laboratory/serializer:
       contain the models serialezers .
       
   ## to run the crud on table "test" the following paths are used
#### method GET
- /api/test - Return a test list
- /api/test/{id} - Return a specific test
#### method post
- /api/test
#### method put
- /api/test/{id}
#### method delete
- /api/test/{id}

 ## to run the crud on table "affiliates" the following paths are used
#### method GET
- /api/affiliate -  Return a affiliate list
- /api/affiliate/{id} -  Return a specific affiliate
#### method post
- /api/affiliate/
#### method put
- /api/affiliate/{id}
#### method delete
- /api/affiliate/{id}

 ## to run the crud on table "appointments" the following paths are used
#### method GET
- /api/appointment/ -  Return a appointment list 
- /api/appointment/{id} - Return a specific appointment
- /api/appointment/affiliates/{id} - Return all the appointments of one affiliate 
- /api/appointment/group/{DATE} - Return all the affiliates with an appointments in specific date
#### method post
- /api/appointment
#### method put
- /api/appointment/{id}
#### method delete
- /api/appointment/{id}
      
  ### technologies
      in ubuntu 22.04
      - mysql       version 8.0.31
      - Django        version 4.1
      
    
  Author

* **Daniel Ruiz Linkedin** - [DanielRuiz](https://www.linkedin.com/in/daniel-ruiz)
