'''
Copies an entire folder and its contents into
a ZIP file whose filename increments
'''
import zipfile, os

def backupToZip(folder):                # Backup the entire contents of "folder" into a ZIP file
    folder = os.path.abspath(folder)    # Make sure the folder is absolute
    # Figure out the filename this code should use based on
    # what files already exists
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):  # Walk the entire folder tree and compress the files in each folder
        print(f'Adding files in {foldername}...')
        backupZip.write(foldername)  # Add the current folder to the ZIP file

        for filename in filenames:  # Add all the files in this folder to the ZIP file
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue            # don't back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
        
    print('Done.')

# backupToZip('')  # insert path that you want to backup