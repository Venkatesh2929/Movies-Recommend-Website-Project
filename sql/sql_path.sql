use moviedb;
CREATE TABLE admin (
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE telugu_movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_name VARCHAR(255),
    cast TEXT,
    summary TEXT,
    release_date DATE,
    ratings DECIMAL(3, 1),
    ott_link VARCHAR(255),
    ott_platform VARCHAR(50),
    category VARCHAR(50)
);


CREATE TABLE hindi_movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_name VARCHAR(255),
    cast TEXT,
    summary TEXT,
    release_date DATE,
    ratings DECIMAL(3, 1),
    ott_link VARCHAR(255),
    ott_platform VARCHAR(50),
    category VARCHAR(50)
);

CREATE TABLE english_movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_name VARCHAR(255),
    cast TEXT,
    summary TEXT,
    release_date DATE,
    ratings DECIMAL(3, 1),
    ott_link VARCHAR(255),
    ott_platform VARCHAR(50),
    category VARCHAR(50)
);


INSERT INTO admin (username, password) VALUES

 ('Admin', 'Admin123');

INSERT INTO telugu_movies (movie_name, cast, summary, release_date, ratings, ott_link, ott_platform, category)
VALUES 
('PUSHPA: The Rise',
 'Directors: Sukumar, Producer: Naveen Yerneni, Y Ravi Shankar, Starring: Allu Arjun, Fahadh Faasil, Rashmika Mandanna',
 'Pushpa Raj (Allu Arjun) is a coolie who volunteers to smuggle red sanders, a rare wood that only grows in Andhra. With novel ideas, Pushpa quickly becomes the leader of a red sanders smuggling network. However, when a ruthless police officer, Bhanwar Singh Shekhawat (Fahadh Faasil), takes charge as SP, he ridicules Pushpa for his lineage.',
 '2021-12-17',
 7.6,
 'https://www.amazon.com',
 'PrimeVideos',
 'Telugu');


select * from telugu_movies;	

	select * from hindi_movies;

	select * from english_movies;

drop table english_movies;

select * from users;

INSERT INTO english_movies (movie_name, cast, summary, release_date, ratings, ott_link, ott_platform, category)
VALUES 
(
    'Godzilla vs. Kong',
    'Directors: Adam Wingard, Producers: Mary Parent, Alex Garcia, Eric McLeod, Brian Rogers, Starring: Alexander Skarsgård, Millie Bobby Brown, Rebecca Hall',
    'Godzilla and Kong clash in a battle for the ages. As Monarch embarks on a mission into uncharted terrain, a human conspiracy threatens to wipe the creatures from the face of the earth.',
    '2021-03-31',
    6.3,
    'https://www.amazon.com',
    'PrimeVideos',
    'English'
),
(
    'Mad Max: Fury Road',
    'Directors: George Miller, Producers: George Miller, Doug Mitchell, P.J. Voeten, Starring: Tom Hardy, Max Rockatansky, Charlize Theron, Furiosa, Nicholas Hoult, Nux',
    'From director George Miller comes the fourth adventure in the Mad Max film series. In a post-apocalyptic world, Max (Hardy) teams up with a mysterious woman, Furiousa (Theron), to try and survive.',
    '2015-05-15',
    8.1,
    'https://www.amazon.com',
    'PrimeVideos',
    'English'
);

INSERT INTO telugu_movies (movie_name, cast, summary, release_date, ratings, ott_link, ott_platform, category)
VALUES 
(
    'Ala Vaikunthapurramuloo',
    'Director: Trivikram Srinivas, Producers: Allu Aravind, S. Radha Krishna, Starring: Allu Arjun, Pooja Hegde, Tabu',
    'A man raised in a wealthy family discovers his true heritage and must navigate the complexities of family dynamics, love, and deception.',
    '2020-01-12',
    8.2,
    'https://www.netflix.com/in/',
    'Netflix',
    'Telugu'
),
(
    'Maharshi',
    'Director: Vamsi Paidipally, Producers: Dil Raju, C. Ashwini Dutt, Prasad V. Potluri, Starring: Mahesh Babu, Pooja Hegde, Allari Naresh',
    'A successful businessman returns to his alma mater and reconnects with his roots, leading to personal and societal transformation.',
    '2019-05-09',
    7.9,
    'https://www.amazon.com',
    'PrimeVideos',
    'Telugu'
),
(
    'Baahubali: The Beginning',
    'Director: S.S. Rajamouli, Producers: Shobu Yarlagadda, Prasad Devineni, Starring: Prabhas, Rana Daggubati, Anushka Shetty',
    'In the kingdom of Mahishmati, a young man rises to fulfill his destiny as the savior of his people and the rightful heir to the throne.',
    '2015-07-10',
    8.1,
    'https://www.netflix.com/in/',
    'Netflix',
    'Telugu'
), 
(
    'RRR',
    'Director: S.S. Rajamouli, Producers: D.V.V. Danayya, Starring: N.T. Rama Rao Jr., Ram Charan, Alia Bhatt, Olivia Morris',
    'Set in the 1920s, RRR revolves around India''s freedom fighters, Alluri Sitarama Raju and Komaram Bheem, who fought against the British Raj and the Nizam of Hyderabad, respectively.',
    '2022-03-24',
    8.2,
    'https://www.netflix.com/in/',
    'Netflix',
    'Telugu'
);



INSERT INTO hindi_movies (movie_name, cast, summary, release_date, ratings, ott_link, ott_platform, category)
VALUES 
(
    'Radhe: Your Most Wanted Bhai',
    'Director: Prabhu Deva, Producers: Salman Khan, Sohail Khan, Atul Agnihotri, Starring: Salman Khan, Disha Patani, Randeep Hooda',
    'A cop is on a mission to eradicate drug abuse and drug dealing from the city, but he faces formidable challenges in the form of a drug lord and his empire.',
    '2021-05-13',
    5.5,
    'https://www.amazon.com',
    'PrimeVideos',
    'Hindi'
),
(
    'Sooryavanshi',
    'Director: Rohit Shetty, Producers: Hiroo Yash Johar, Karan Johar, Apoorva Mehta, Rohit Shetty, Starring: Akshay Kumar, Katrina Kaif, Ajay Devgn',
    'A top cop sets out to thwart a terrorist attack in Mumbai, but he must also confront personal challenges and conflicts along the way.',
    '2021-11-05',
    6.9,
    'https://www.netflix.com/in/',
    'Netflix',
    'Hindi'
),
(
    'Gangs of Wasseypur',
    'Director: Anurag Kashyap, Producers: Anurag Kashyap, Sunil Bohra, Starring: Manoj Bajpayee, Richa Chadha, Nawazuddin Siddiqui',
    'A gritty saga of power, revenge, and politics unfolds in the coal-rich town of Wasseypur, spanning multiple generations and rivalries.',
    '2012-06-22',
    8.2,
    'https://www.zee5.com',
    'ZEE5',
    'Hindi'
),
(
    'Tanu Weds Manu',
    'Director: Aanand L. Rai, Producers: Shailesh R. Singh, Surya Singh, Starring: Kangana Ranaut, R. Madhavan, Jimmy Sheirgill',
    'Opposites attract in this quirky romantic comedy, as an eccentric girl and a sensible man navigate love, family, and societal expectations.',
    '2011-02-25',
    7.6,
    'https://www.hotstar.com',
    'Hotstar',
    'Hindi'
),
(
    'Andhadhun',
    'Director: Sriram Raghavan, Producers: Sanjay Routray, Matchbox Pictures, Viacom18 Motion Pictures, Starring: Ayushmann Khurrana, Tabu, Radhika Apte',
    'A blind pianist gets entangled in a web of murder, deceit, and intrigue after witnessing a crime, leading to a thrilling cat-and-mouse chase.',
    '2018-10-05',
    8.3,
    'https://www.zee5.com',
    'ZEE5',
    'Hindi'
);


INSERT INTO english_movies (movie_name, cast, summary, release_date, ratings, ott_link, ott_platform, category)
VALUES 
(
    'The Shawshank Redemption',
    'Director: Frank Darabont, Producers: Niki Marvin, Starring: Tim Robbins, Morgan Freeman, Bob Gunton',
    'A poignant tale of hope, friendship, and redemption unfolds in a maximum-security prison as two inmates forge an unbreakable bond.',
    '1994-10-14',
    9.3,
    'https://www.zee5.com',
    'ZEE5',
    'English'
),
(
    'The Dark Knight',
    'Director: Christopher Nolan, Producers: Christopher Nolan, Charles Roven, Starring: Christian Bale, Heath Ledger, Aaron Eckhart',
    'The Caped Crusader faces his greatest challenge yet as he battles the anarchic Joker, who seeks to plunge Gotham City into chaos.',
    '2008-07-18',
    9.0,
    'https://www.zee5.com',
    'ZEE5',
    'English'
);