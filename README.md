Follow the following steps:

1. Open command prompt/terminal
2. Change the current working directory to the location where you want the cloned directory to be made.
3. Then enter the following command in it:
    git clone https://github.com/ayush7garg/covinassign.git
4. Press enter.
   You can see a folder by the name "covinassign" in your working directory.
5. Now, again open command prompt/terminal.
6. Enter the following command:
    python manage.py createsuperuser
7. Then enter a username of your choice
8. Then it will ask for your email.
9. Then enter a strong password
10. After that, you can see a messaage saying: "Superuser created successfully."
11. Now enter the following command in the command prompt:
    python manage.py runserver
12. After running the above command, number of lines will appear, one of those lines will look like this:
    Starting development server at http://127.0.0.1:8000/
13. You may get a different server location.
14. Now enter the provided server address in any browser window.
15. Now enter the same Username and password that you used while creating the superuser.
16. The django administration window will open in the browser window.
17. Under the app name 'CALLANALYZER', you can see a madel named 'Calls'. Click on it.
18. After that, you will be taken to another page. Click on 'Add Call' button on the top-right of the page.
19. Now upload a text file in the 'File' field and enter some text in the 'Char' field.
20. Click on 'Save' button.
21. You will see a message in green color on the top of the window saying "The call “call object (1)” was added successfully."
22. If you get this message, it means that you have done everything correctly, otherwise go through the above steps once more.
23. You can see all the created call objects and you can also delete any of these.
24. For API framework, enter the following URL in your browser window:
    "http://127.0.0.1:8000/files/"
25. The Django REST framework page will open. With this page, you can only upload your files, you cannot see the previously uploaded files by you or any other user.
26. This is because here you are the esternal party for application. You can only provide your files, but you cannot access them.
