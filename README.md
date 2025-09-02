To run the project, the first thing that you need to do is open the Django project. Then, you use command "cd office" in your terminal and type "python manage.py runserver". By doing this, the application runs. Do note that KYCForm is in its initial stages, that's why there are several types of issues. 

You can easily logins directly typing "http://127.0.0.1:8000/kyc_login/". Your page loads, where you can find two fields, particularly Policy Number and Date of birth for each individual policy holder with a unique identity. The front-end and back-end integration is not perfect due to an external API not completely developed.
When it comes to the KYC form, you can type "http://127.0.0.1:8000/kyc_form/" which directs you to the main "KYC form page" in which policy holder submitting their personal and other financial details.

Once you provide the form with the mandatory details, the next thing you should focus on is viewing the form that comes in "http://127.0.0.1:8000/kyc_list/". The CRUD operation is utilised to offer you the update, view, and delete of the present data. 
There is also "http://127.0.0.1:8000/kyc_lists/". This specific page is designed for admin side or simply agent part.

The thing that you need to keep in mind is that database that's opted for is 'SQL server'. Not only this, it is not difficult to change your database option from SQL server to dbsqlite, Postgresql or Mysql inside SETTINGS.



