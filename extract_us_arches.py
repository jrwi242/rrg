
# coding: utf-8

# In[1]:


# Python 3
# -----Find Arches by elevaton -----#
# by joyrwGIS for GEO 409. Uky
# Fall 2018
# ------ ------#


# In[2]:


# Import site package for ArcGIS
import arcpy


# In[3]:


# Set ArcGIS evironment
arcpy.env.workspace = r"C:\GIS\geology.gdb"
arcpy.env.overwriteOutput = True


# In[4]:


# Set Local Variables
intable = "arches_by_elev.csv"
outLocation = "C:\GIS\joyrwGIS\409\geo409-module-02-jrwi242"
outTable ="ky_arches_over1000ft.csv" 


# In[5]:


# Assign variables
input_layer = "us_arches"
output_path = r"C:\GIS"


# In[6]:


# Prompt for user input
print("This program returns all arches as .csv file at or above the minimum elevation.")
elevationNumber = input("Enter minimum elevation: ")


# In[7]:


# Adding Additional Functions
State = input("Enter State Name: ")


# In[8]:


# Try converting to integer. Exit if not integer
try:
    elevationNumber = int(elevation)
except:
    print("Whoops! Try using a number.")
exit()


# In[9]:


# Build the where clause, aka the SQL statement to select features
whereClause = "base_elevation_ft >= " + str(elevationNumber)


# In[10]:


# Use the TableToTable arcpy function extract by SQL query
arcpy.TableToTable_conversion (input_layer, output_path, "arches_by_elev.csv", whereClause)

