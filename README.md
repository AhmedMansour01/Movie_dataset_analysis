# Movie_dataset_analysis
Analyzing tmdb movie datasets using SQL, Python pandas, Excel, and Tableau. 
The purpose of this project is to combine some of the skills that I have learned in my data analysis learning journey. combining a little bit of everything together in this project.


## Skills used:

1. Python Pandas
2. SQL.
3. PostgreSQL.
4. Excel PowerQuery.
5. Excel Pivot Tables.
6. Tableau.


## Cleaning and preparing the data:

I started with two files: a movies file and a credits files. I needed a file for the genres so that was the part I decided to analyze. 
so using Python Pandas I began moving the data and cleaning it until I had the data that I needed:

![create_genres](https://github.com/user-attachments/assets/70792cd0-9c83-4c14-9bf5-2aa3864b219c)


![clean_genres](https://github.com/user-attachments/assets/4eed5da0-5641-45de-b8bc-003d26ad4691)


![create_genres-columns](https://github.com/user-attachments/assets/d03d403f-ae2c-480e-aa8a-1357146471a5)


![remove_unwanted](https://github.com/user-attachments/assets/fab870a2-5abd-436d-aad9-8a0baec14f34)

## creating the SQL database:

while it was necessary, I went ahead and created some data tables in a PostgreSQL database I set up:

![create_movie_table](https://github.com/user-attachments/assets/30bc85a4-d497-4614-9d0d-3605084a29ae)

![create_credits genres_tables](https://github.com/user-attachments/assets/66252496-1b19-4373-9e18-85a2d21f19f0)


## Importing the data and writing the query:

now that the data was in the database, it was time to import the datasets into the tables and write the query:

![importing_data](https://github.com/user-attachments/assets/c3ab6b3d-33ed-4caf-8b40-9c3a89ab2997)

![tmdb_query](https://github.com/user-attachments/assets/49000252-2ecd-4433-ad84-d75dbf7d11be)

## Further cleaning and organizing in Excel:

after importing the data into a CSV file, I opened it using Excel and began polishing things using Power Pivot:

Here is the before:
![data-before-transforming](https://github.com/user-attachments/assets/f715f1b2-70f7-4171-a7ee-13a01607cbd3)

Here is the After:
![data-after-transforming](https://github.com/user-attachments/assets/a31ac5f7-f6ea-4c65-9a3f-46ccbd017ec0)


## Pivot Table:
I created a pivot table and added some conditional formatting to gain insights:

![tmdb_pivottable](https://github.com/user-attachments/assets/71c09817-e685-4dcc-8996-fda538baf1df)


## Tabluea Dashboard:
created a quick viz in Tableau that provides basically the same insights as the Pivot Tables:

![Tableau_vis](https://github.com/user-attachments/assets/187a3a6f-7726-409a-9660-1b966f4a03ef)


### Final words:
This was fun. Maybe not the best demonstration of my skills but I'm glad I did it.

