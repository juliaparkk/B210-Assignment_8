# B210-Assignment_8
# a. What is the purpose of this program(s)?
The purpose of this program is to write a function that creates a tuple of song names, then sorts that tuple based on album_release_date and writes to a new CSV file.
# b. What does the program do, including what it takes for input, and what it gives as output?
The program reads the whole CSV as lines, parses the header and finds the indices for track_name and album_release_date, parses fields with split_csv_line, collects pairs (album_release_date, track_name), and sorts the collected pairs by album_release_date lexicographically (ISO YYYY-MM-DD strings sort chronologically).
The input is the CSV file: taylor_discography.csv. However, the track_name and album_release_date columns are required.
The output is a tuple of sorted track names (oldest → newest) returned by the function, and a CSV file written to output_csv_path (by default, sorted_tracks_by_release.csv) with two columns: track_name, album_release_date.
When run as a script, it prints:
Wrote <output path>
Total tracks written: <n>
The first 10 track names (oldest → newest).
# c. How do you use the program?
After copying and pasting the code into VSCode, 
Save file: Save the code as C:\Users\jinas\Downloads\Assignment 8 Tuples and Sets.py.
Please make sure the input CSV file exists; by default, the script expects taylor_discography.csv. You can either place your CSV there or edit the input_csv variable near the bottom of the file.
Run the script (PowerShell)
If Python is on your PATH:
Python "C:\Users\jinas\Downloads\Assignment 8 Tuples and Sets.py"
Or you can click the run button through VSCode. 
Example printed lines:
Wrote C:\Users\jinas\Downloads\sorted_tracks_by_release.csv
Total tracks written: 434
First 10 tracks (oldest→newest): followed by the first 10 track names
