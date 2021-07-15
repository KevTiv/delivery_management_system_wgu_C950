
Scenario:

# delivery_management_system_wgu_C950
The Western Governors University Parcel Service (WGUPS) needs to determine the best route and delivery distribution for their Daily Local Deliveries (DLD) because packages  are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver  each day; each package has specific criteria and delivery requirements.  Your task is to determine the best algorithm, write code, and present a solution where all 40 packages, listed in the attached “WGUPS Package File,” will be delivered on time  with the least number of miles added to the combined mileage total of all trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map” and  distances to each location are given in the attached “WGUPS Distance Table.”  While you work on this assessment, take into consideration the specific delivery time expected for each package and the possibility that the delivery requirements—including the  expected delivery time—can be changed by management at any time and at any point along the chosen route. In addition, you should keep in mind that the supervisor should be  able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the “WGUPS Package File,” including what  has been delivered and what time the delivery occurred.  The intent is to use this solution (program) for this specific location and to use the same program in many cities in each state where WGU has a presence. As such, you will need to  include detailed comments, following the industry-standard Python style guide, to make your code easy to read and to justify the decisions you made while writing your program.

Assumptions:

    Each truck can carry a maximum of 16 packages.
    Trucks travel at an average speed of 18 miles per hour.
    Trucks have a “infinite amount of gas” with no need to stop.
    Each driver stays with the same truck as long as that truck is in service.
    Drivers leave the hub at 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. The day ends when all 40 packages have been delivered.
    Delivery time is instantaneous, i.e., no time passes while at a delivery (that time is factored into the average speed of the trucks).
    There is up to one special note for each package.
    The package ID is unique; there are no collisions.
    No further assumptions exist or are allowed.


Project Run Result:

Truck 1 is leaving at 8:00 AM
Traveling from Western Governors University -> Cottonwood Regional Softball Complex, distance is 1.9 miles away and it should take 6.33 minutes
Package 14 was delivered to 4300 S 1300 E, Millcreek, UT 84117 at 08:06 AM, Deadline was 10:30 AM
Traveling from Cottonwood Regional Softball Complex -> Holiday City Office, distance is 2.0 miles away and it should take 6.67 minutes
Package 15 was delivered to 4580 S 2300 E, Holladay, UT 84117 at 08:13 AM, Deadline was 9:00 AM
Package 16 was delivered to 4580 S 2300 E, Holladay, UT 84117 at 08:13 AM, Deadline was 10:30 AM
Package 34 was delivered to 4580 S 2300 E, Holladay, UT 84117 at 08:13 AM, Deadline was 10:30 AM
Traveling from Holiday City Office -> Sugar House Park, distance is 5.0 miles away and it should take 16.67 minutes
Package 29 was delivered to 1330 2100 S, Salt Lake City, UT 84106 at 08:29 AM, Deadline was 10:30 AM
Package 7 was delivered to 1330 2100 S, Salt Lake City, UT 84106 at 08:29 AM
Traveling from Sugar House Park -> South Salt Lake Public Works, distance is 2.8 miles away and it should take 9.33 minutes
Package 1 was delivered to 195 W Oakland Ave, Salt Lake City, UT 84115 at 08:39 AM, Deadline was 10:30 AM
Traveling from South Salt Lake Public Works -> Utah DMV Administrative Office, distance is 1.1 miles away and it should take 3.67 minutes
Package 40 was delivered to 380 W 2880 S, Salt Lake City, UT 84115 at 08:42 AM, Deadline was 10:30 AM
Traveling from Utah DMV Administrative Office -> Housing Auth. of Salt Lake County, distance is 1.6 miles away and it should take 5.33 minutes
Package 20 was delivered to 3595 Main St, Salt Lake City, UT 84115 at 08:48 AM, Deadline was 10:30 AM
Traveling from Housing Auth. of Salt Lake County -> Salt Lake City Division of Health Services, distance is 0.5 miles away and it should take 1.67 minutes
Package 19 was delivered to 177 W Price Ave, Salt Lake City, UT 84115 at 08:49 AM
Traveling from Salt Lake City Division of Health Services -> Salt Lake County/United Police Dept, distance is 2.7 miles away and it should take 9.0 minutes
Package 31 was delivered to 3365 S 900 W, Salt Lake City, UT 84119 at 08:58 AM, Deadline was 10:30 AM
Traveling from Salt Lake County/United Police Dept -> Salt Lake City Streets and Sanitation, distance is 5.8 miles away and it should take 19.33 minutes
Package 13 was delivered to 2010 W 500 S, Salt Lake City, UT 84104 at 09:18 AM, Deadline was 10:30 AM
Traveling from Salt Lake City Streets and Sanitation -> Third District Juvenile Court, distance is 3.2 miles away and it should take 10.67 minutes
Package 37 was delivered to 410 S State St, Salt Lake City, UT 84111 at 09:28 AM, Deadline was 10:30 AM
Package 5 was delivered to 410 S State St, Salt Lake City, UT 84111 at 09:28 AM
Traveling from Third District Juvenile Court -> Council Hall, distance is 1.0 miles away and it should take 3.33 minutes
Package 30 was delivered to 300 State St, Salt Lake City, UT 84103 at 09:32 AM, Deadline was 10:30 AM
Package 8 was delivered to 300 State St, Salt Lake City, UT 84103 at 09:32 AM
Traveling from Council Hall -> Western Governors University, distance is 7.6 miles away and it should take 25.33 minutes
Final time: 09:57 AM
Total Distance: 35.2 miles
Truck 2 is leaving at 9:05 AM
Traveling from Western Governors University -> Housing Auth. of Salt Lake County, distance is 2.0 miles away and it should take 6.67 minutes
Package 21 was delivered to 3595 Main St, Salt Lake City, UT 84115 at 09:11 AM
Traveling from Housing Auth. of Salt Lake County -> South Salt Lake Police, distance is 1.2 miles away and it should take 4.0 minutes
Package 28 was delivered to 2835 Main St, Salt Lake City, UT 84115 at 09:15 AM
Traveling from South Salt Lake Police -> Columbus Library, distance is 1.1 miles away and it should take 3.67 minutes
Package 33 was delivered to 2530 S 500 E, Salt Lake City, UT 84106 at 09:19 AM
Traveling from Columbus Library -> Salt Lake County Mental Health, distance is 3.7 miles away and it should take 12.33 minutes
Package 17 was delivered to 3148 S 1100 W, Salt Lake City, UT 84119 at 09:31 AM
Traveling from Salt Lake County Mental Health -> Salt Lake County/United Police Dept, distance is 0.6 miles away and it should take 2.0 minutes
Package 32 was delivered to 3365 S 900 W, Salt Lake City, UT 84119 at 09:33 AM
Traveling from Salt Lake County/United Police Dept -> Redwood Park, distance is 1.5 miles away and it should take 5.0 minutes
Package 6 was delivered to 3060 Lester St, West Valley City, UT 84119 at 09:38 AM, Deadline was 10:30 AM
Traveling from Redwood Park -> Deker Lake, distance is 1.6 miles away and it should take 5.33 minutes
Package 36 was delivered to 2300 Parkway Blvd, West Valley City, UT 84119 at 09:44 AM
Traveling from Deker Lake -> Taylorsville-Bennion Heritage City Gov Off, distance is 4.0 miles away and it should take 13.33 minutes
Package 18 was delivered to 1488 4800 S, Salt Lake City, UT 84123 at 09:57 AM
Traveling from Taylorsville-Bennion Heritage City Gov Off -> Valley Regional Softball Complex, distance is 0.6 miles away and it should take 2.0 minutes
Package 23 was delivered to 5100 South 2700 West, Salt Lake City, UT 84118 at 09:59 AM
Traveling from Valley Regional Softball Complex -> Taylorsville City Hall, distance is 0.4 miles away and it should take 1.33 minutes
Package 11 was delivered to 2600 Taylorsville Blvd, Salt Lake City, UT 84118 at 10:00 AM
Traveling from Taylorsville City Hall -> City Center of Rock Springs, distance is 4.9 miles away and it should take 16.33 minutes
Package 25 was delivered to 5383 South 900 East #104, Salt Lake City, UT 84117 at 10:17 AM, Deadline was 10:30 AM
Package 26 was delivered to 5383 South 900 East #104, Salt Lake City, UT 84117 at 10:17 AM
Traveling from City Center of Rock Springs -> Third District Juvenile Court, distance is 8.5 miles away and it should take 28.33 minutes
Package 38 was delivered to 410 S State St, Salt Lake City, UT 84111 at 10:45 AM
Traveling from Third District Juvenile Court -> Salt Lake City Ottinger Hall, distance is 1.0 miles away and it should take 3.33 minutes
Package 3 was delivered to 233 Canyon Rd, Salt Lake City, UT 84103 at 10:48 AM
Traveling from Salt Lake City Ottinger Hall -> Salt Lake City Streets and Sanitation, distance is 4.2 miles away and it should take 14.0 minutes
Package 39 was delivered to 2010 W 500 S, Salt Lake City, UT 84104 at 11:02 AM
Traveling from Salt Lake City Streets and Sanitation -> Western Governors University, distance is 10.9 miles away and it should take 36.33 minutes
Final time: 11:39 AM
Total Distance: 46.2 miles
Truck 3 is leaving at 10:20 AM
Traveling from Western Governors University -> Murray City Museum, distance is 2.4 miles away and it should take 8.0 minutes
Package 24 was delivered to 5025 State St, Murray, UT 84107 at 10:28 AM
Traveling from Murray City Museum -> Wheeler Historic Farm, distance is 3.1 miles away and it should take 10.33 minutes
Package 22 was delivered to 6351 South 900 East, Murray, UT 84121 at 10:38 AM
Traveling from Wheeler Historic Farm -> Columbus Library, distance is 6.0 miles away and it should take 20.0 minutes
Package 2 was delivered to 2530 S 500 E, Salt Lake City, UT 84106 at 10:58 AM
Traveling from Columbus Library -> Utah DMV Administrative Office, distance is 1.8 miles away and it should take 6.0 minutes
Package 4 was delivered to 380 W 2880 S, Salt Lake City, UT 84115 at 11:04 AM
Traveling from Utah DMV Administrative Office -> Rice Terrace Pavilion Park, distance is 4.3 miles away and it should take 14.33 minutes
Package 10 was delivered to 600 E 900 South, Salt Lake City, UT 84105 at 11:18 AM
Traveling from Rice Terrace Pavilion Park -> Third District Juvenile Court, distance is 1.8 miles away and it should take 6.0 minutes
Package 9 was delivered to 410 S State St, Salt Lake City, UT 84111 at 11:24 AM
Traveling from Third District Juvenile Court -> International Peace Gardens, distance is 4.8 miles away and it should take 16.0 minutes
Package 35 was delivered to 1060 Dalton Ave S, Salt Lake City, UT 84104 at 11:40 AM
Package 27 was delivered to 1060 Dalton Ave S, Salt Lake City, UT 84104 at 11:40 AM
Traveling from International Peace Gardens -> West Valley Prosecutor, distance is 7.4 miles away and it should take 24.67 minutes
Package 12 was delivered to 3575 W Valley Central Station bus Loop, West Valley City, UT 84119 at 12:05 PM
Traveling from West Valley Prosecutor -> Western Governors University, distance is 7.6 miles away and it should take 25.33 minutes
Final time: 12:30 PM
Total Distance: 39.2 miles
Total miles traveled: 120.6
