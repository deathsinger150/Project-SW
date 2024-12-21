CREATE DATABASE ClubManagementSystem;
USE ClubManagementSystem;

CREATE TABLE Clubs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    club_name VARCHAR(100) UNIQUE NOT NULL,
    Clubs_description TEXT
);
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    joined_clubs TEXT, 	
    email VARCHAR(255) UNIQUE NOT NULL,
    Users_role ENUM('Student', 'Admin', 'ClubMember', 'ClubBoardMember') DEFAULT 'Student',
    Users_password VARCHAR(255) NOT NULL
);
CREATE TABLE Admins (
    id INT PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES Users(id)
);

CREATE TABLE ClubBoardMembers (
    club_id INT,
    user_id INT,
    position VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (club_id) REFERENCES Clubs(id) ON DELETE CASCADE
);

CREATE TABLE ClubCommittees (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each committee
    club_id INT NOT NULL,              -- Foreign key to the club
    committee_name VARCHAR(255) NOT NULL, -- Name of the committee
    FOREIGN KEY (club_id) REFERENCES Clubs(id) ON DELETE CASCADE
);


CREATE TABLE ClubMembers (
    club_id INT NOT NULL,              -- Foreign key to the club
    user_id INT NOT NULL,              -- Foreign key to the user
    Club_member_committee INT,         -- Foreign key to the committee (if the member belongs to one)
    FOREIGN KEY (club_id) REFERENCES Clubs(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (Club_member_committee) REFERENCES ClubCommittees(id) ON DELETE SET NULL
);


CREATE TABLE ClubAchievements (
    club_id INT,
    admin_id INT,
    achievement TEXT,
    date_awarded DATE,
    FOREIGN KEY (admin_id) REFERENCES Admins(id) ON DELETE CASCADE,
    FOREIGN KEY (club_id) REFERENCES Clubs(id) ON DELETE CASCADE
);

CREATE TABLE Events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
	club_name VARCHAR(255) NOT NULL,
    event_name VARCHAR(255) ,
    Events_description TEXT,
    club_id INT,
    admin_id INT,
    location VARCHAR(255),
    staff_list TEXT, 
    sponsors TEXT, 
    Events_date DATE,
    
    FOREIGN KEY (admin_id) REFERENCES Admins(id) ON DELETE CASCADE,
    FOREIGN KEY (club_id) REFERENCES Clubs(id) ON DELETE CASCADE
);

CREATE TABLE Sessions (
    track_sessions INT PRIMARY KEY,
    club_name VARCHAR(255) NOT NULL,
    club_id INT,
    admin_id INT,
    instructor_id INT,
    Sessions_schedule TEXT, 
    attendance_count INT,
    material_file VARCHAR(255),
    FOREIGN KEY (admin_id) REFERENCES Admins(id) ON DELETE CASCADE,
    FOREIGN KEY (club_id) REFERENCES Clubs(id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES Users(id) ON DELETE SET NULL
);

CREATE TABLE Collaboration (
    applying_club_id INT NOT NULL,
    receiving_club_id INT NOT NULL,
    applying_admin_id INT NOT NULL,
    receiving_admin_id INT NOT NULL,
    collaboration_description TEXT,
    collaboration_status ENUM('Pending', 'Accepted', 'Rejected') DEFAULT 'Pending',
    application_date DATE,
    FOREIGN KEY (applying_club_id) REFERENCES Clubs(id) ON DELETE CASCADE,
    FOREIGN KEY (receiving_club_id) REFERENCES Clubs(id) ON DELETE CASCADE,
    FOREIGN KEY (applying_admin_id) REFERENCES Admins(id) ON DELETE CASCADE,
    FOREIGN KEY (receiving_admin_id) REFERENCES Admins(id) ON DELETE CASCADE
);


INSERT INTO Clubs (club_name, Clubs_description)
VALUES
('RPM CLUB', 'A club dedicated to enthusiasts of robotics, 
programming, and machine learning, providing a platform for learning, e
xperimentation, and collaboration in these fields.'),
('ICPC CLUB', 'A club for students passionate about competitive programming,
 problem-solving, and algorithm design, encouraging creativity and teamwork in
 coding challenges.'),
('GDG CLUB', 'A club focused on technology, innovation, and Google’s developer ecosystem,
 offering events and resources to help members grow in software development 
 and entrepreneurship.');

INSERT INTO Users (user_name, joined_clubs, email, Users_role, Users_password)
VALUES
('Mohamed Hossam', 'ICPC CLUB', 'm.hossam2201@nu.edu.eg', 'Admin', SHA2('password123', 256)),
('seif kassab', 'ICPC CLUB', 's.kassab2250@nu.edu.eg', 'Student', SHA2('securepassword', 256)),
('Ranim hisham', 'RPM CLUB', 'r.hisham2210@nu.edu.eg', 'ClubBoardMember', SHA2('mypassword', 256)),
('omar mohamed', 'GDG CLUB', 'o.mohamed2230@nu.edu.eg', 'ClubMember', SHA2('password456', 256)),
('Farida amr', 'RPM', 'f.Amr2237@nu.edu.eg', 'Admin', SHA2('password789', 256));

INSERT INTO ClubCommittees (club_id, committee_name)
VALUES
-- Committees for RPM CLUB (club_id = 1)
(1, 'HR'),
(1, 'PR'),
(1, 'Operations'),
(1, 'Social Media'),
(1, 'Media'),
(1, 'Technical'),

-- Committees for ICPC CLUB (club_id = 2)
(2, 'HR'),
(2, 'PR'),
(2, 'Operations'),
(2, 'Social Media'),
(2, 'Media'),
(2, 'Technical'),

-- Committees for GDG CLUB (club_id = 3)
(3, 'HR'),
(3, 'PR'),
(3, 'Operations'),
(3, 'Social Media'),
(3, 'Media'),
(3, 'Technical');

select* from ClubCommittees ;

DELETE FROM ClubCommittees;




