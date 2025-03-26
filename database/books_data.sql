-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: bookstore
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `books_data`
--

LOCK TABLES `books_data` WRITE;
/*!40000 ALTER TABLE `books_data` DISABLE KEYS */;
INSERT INTO `books_data` VALUES (9780002740234,'Keep It Simple: And Get More Out of Life','Nick Page',1999,'Trafalgar Square','http://images.amazon.com/images/P/0002740230.01.LZZZZZZZ.jpg',4.8,249,3052),(9780006513407,'Making Minty Malone','Isabel Wolff',2000,'Onyx Books','http://images.amazon.com/images/P/0451409256.01.LZZZZZZZ.jpg',3.7,299,4352),(9780007116836,'A Monk Swimming','Malachy McCourt',1998,'Hyperion','http://images.amazon.com/images/P/0786863986.01.LZZZZZZZ.jpg',4.7,349,1988),(9780008475918,'The Patient','Michael Palmer',2001,'Bantam Books','http://images.amazon.com/images/P/0553580388.01.LZZZZZZZ.jpg',4.6,249,2229),(9780060163709,'Coyote Waits (Joe Leaphorn/Jim Chee Novels)','Tony Hillerman',1992,'HarperTorch','http://images.amazon.com/images/P/0061099325.01.LZZZZZZZ.jpg',4.8,199,3978),(9780060506070,'Clara Callan','Richard Bruce Wright',2001,'HarperFlamingo Canada','http://images.amazon.com/images/P/0002005018.01.LZZZZZZZ.jpg',4.6,249,354),(9780060563073,'Peter Pan: The Original Story (Peter Pan)','J. M. Barrie',2003,'HarperFestival','http://images.amazon.com/images/P/0060563079.01.LZZZZZZZ.jpg',4.6,349,1514),(9780060850524,'1984','George Orwell',1949,'Secker & Warburg','https://m.media-amazon.com/images/I/91VsLImyJgL._SL1500_.jpg',4.4,210,7800),(9780060935467,'To Kill a Mockingbird','Harper Lee',1988,'Little Brown &amp; Company','http://images.amazon.com/images/P/0446310786.01.LZZZZZZZ.jpg',4.8,249,3769),(9780060938413,'The Accidental Virgin','Valerie Frankel',2003,'Avon Trade','http://images.amazon.com/images/P/0060938412.01.LZZZZZZZ.jpg',4.6,399,393),(9780060976842,'Little Altars Everywhere: A Novel','Rebecca Wells',1996,'Perennial','http://images.amazon.com/images/P/0060976845.01.LZZZZZZZ.jpg',4.3,249,3446),(9780061052521,'Interesting Times: A Novel of Discworld','Terry Pratchett',1997,'Harpercollins','http://images.amazon.com/images/P/0061052523.01.LZZZZZZZ.jpg',4.3,199,47),(9780061076039,'Mary-Kate &amp; Ashley Switching Goals (Mary-Kate and Ashley Starring in)','Mary-Kate &amp; Ashley Olsen',2000,'HarperEntertainment','http://images.amazon.com/images/P/0061076031.01.LZZZZZZZ.jpg',3.7,299,2824),(9780061120091,'One Hundred Years of Solitude','Gabriel Garcia Marquez',1998,'Perennial','http://images.amazon.com/images/P/0060929790.01.LZZZZZZZ.jpg',4.7,399,3679),(9780061374630,'My Friend Flicka','Mary O\'Hara',1988,'Perennial','http://images.amazon.com/images/P/0060809027.01.LZZZZZZZ.jpg',4.8,399,1001),(9780062024022,'Divergent','Veronica Roth',2011,'Katherine Tegen Books','https://m.media-amazon.com/images/I/81H1MhBbPbL._SL1500_.jpg',4.1,270,4600),(9780099280255,'The Brethren','John Grisham',2000,'Doubleday','http://images.amazon.com/images/P/0385497466.01.LZZZZZZZ.jpg',3.7,249,2287),(9780099416173,'The King of Torts','John Grisham',2003,'Doubleday Books','http://images.amazon.com/images/P/0385508042.01.LZZZZZZZ.jpg',4.6,299,3621),(9780099427575,'Tree Grows In Brooklyn','Betty Smith',1988,'Harpercollins Publisher','http://images.amazon.com/images/P/0060801263.01.LZZZZZZZ.jpg',4.8,299,2109),(9780099429326,'Crow Lake (Today Show Book Club #7)','Mary Lawson',2003,'Delta','http://images.amazon.com/images/P/0385337639.01.LZZZZZZZ.jpg',4.6,249,4271),(9780099771517,'Memoirs of a Geisha','Arthur Golden',1997,'Alfred A. Knopf','http://images.amazon.com/images/P/0375400117.01.LZZZZZZZ.jpg',4.3,349,421),(9780140082906,'The Mosquito Coast','Paul Theroux',1990,'Harper Mass Market Paperbacks (Mm)','http://images.amazon.com/images/P/0380619458.01.LZZZZZZZ.jpg',4.8,349,2388),(9780140244427,'Eva Luna','Isabel Allende',1989,'Bantam Books','http://images.amazon.com/images/P/0553280589.01.LZZZZZZZ.jpg',4.8,349,1853),(9780140620665,'Mansfield Park (Penguin Popular Classics)','Jane Austen',1994,'Penguin Books Ltd','http://images.amazon.com/images/P/0140620664.01.LZZZZZZZ.jpg',4.6,199,1585),(9780141000190,'Bridget Jones\'s Diary','Helen Fielding',1997,'Picador (UK)','http://images.amazon.com/images/P/0330332775.01.LZZZZZZZ.jpg',4.3,249,3529),(9780141023649,'Secret History','Donna Tartt',1993,'Ballantine Books','http://images.amazon.com/images/P/0804111359.01.LZZZZZZZ.jpg',4.8,299,887),(9780143028574,'The God of Small Things','Arundhati Roy',1998,'Perennial','http://images.amazon.com/images/P/0060977493.01.LZZZZZZZ.jpg',4.7,399,4455),(9780143038108,'The Kitchen God\'s Wife','Amy Tan',1991,'Putnam Pub Group','http://images.amazon.com/images/P/0399135782.01.LZZZZZZZ.jpg',4.8,299,4930),(9780151002177,'Animal Farm','George Orwell',2004,'Signet','http://images.amazon.com/images/P/0451526341.01.LZZZZZZZ.jpg',4.6,349,44),(9780151836000,'A Soldier of the Great War','Mark Helprin',1992,'Avon Books','http://images.amazon.com/images/P/0380715899.01.LZZZZZZZ.jpg',4.8,399,132),(9780156027328,'Life of Pi','Yann Martel',2002,'Harcourt','http://images.amazon.com/images/P/0151008116.01.LZZZZZZZ.jpg',4.6,349,1191),(9780197653920,'Classical Mythology','Mark P. O. Morford',2002,'Oxford University Press','http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg',4.6,349,1201),(9780241558331,'James and the Giant Peach','Roald Dahl',2002,'Knopf Books for Young Readers','http://images.amazon.com/images/P/0375814248.01.LZZZZZZZ.jpg',4.6,299,2269),(9780297847328,'The Right Man : The Surprise Presidency of George W. Bush','David Frum',2003,'Random House','http://images.amazon.com/images/P/0375509038.01.LZZZZZZZ.jpg',4.6,399,1648),(9780307277671,'The Da Vinci Code','Dan Brown',2003,'Doubleday','https://m.media-amazon.com/images/I/913CifLtXeL._SL1500_.jpg',4.5,225,4500),(9780307387899,'The Kite Runner','Khaled Hosseini',2003,'Riverhead Books','https://m.media-amazon.com/images/I/81LVEH25iJL._SL1500_.jpg',4.6,330,5900),(9780312854676,'Proxies','Laura J. Mixon',1999,'Tor Books','http://images.amazon.com/images/P/0812523873.01.LZZZZZZZ.jpg',4.8,249,2696),(9780312872687,'The James Dean Affair: A Neil Gulliver &amp; Stevie Marriner Novel','Robert S. Levinson',2000,'St Martins Pr','http://images.amazon.com/images/P/0312872682.01.LZZZZZZZ.jpg',3.7,299,1990),(9780312890049,'Moonheart (Newford)','Charles de Lint',1994,'Orb Books','http://images.amazon.com/images/P/0312890044.01.LZZZZZZZ.jpg',4.7,349,4913),(9780312970246,'The Angel Is Near','Deepak Chopra',2000,'St. Martin\'s Press','http://images.amazon.com/images/P/0312970242.01.LZZZZZZZ.jpg',3.7,399,3235),(9780312980153,'Fast Women','Jennifer Crusie',2001,'St. Martin\'s Press','http://images.amazon.com/images/P/0312252617.01.LZZZZZZZ.jpg',4.6,399,467),(9780316010368,'All He Ever Wanted: A Novel','Anita Shreve',2004,'Back Bay Books','http://images.amazon.com/images/P/0316735736.01.LZZZZZZZ.jpg',4.6,399,390),(9780316010689,'Downtown','Anne Rivers Siddons',1995,'HarperTorch','http://images.amazon.com/images/P/0061099686.01.LZZZZZZZ.jpg',4.3,399,1419),(9780316097505,'The Gospel of Judas: A Novel','Simon Mawer',2002,'Back Bay Books','http://images.amazon.com/images/P/0316973742.01.LZZZZZZZ.jpg',4.6,299,53),(9780316748643,'Pasquale\'s Nose: Idle Days in an Italian Town','Michael Rips',2002,'Back Bay Books','http://images.amazon.com/images/P/0316748641.01.LZZZZZZZ.jpg',4.6,349,2245),(9780316769488,'The Catcher in the Rye','J.D. Salinger',1951,'Little, Brown and Company','https://m.media-amazon.com/images/I/71nXPGovoTL._SL1500_.jpg',4.0,225,5000),(9780330484510,'Twenty Minute Retreats: Revive Your Spirits in Just Minutes a Day (A Pan Self-discovery Title)','Rachel Harris',2001,'Pan Macmillan','http://images.amazon.com/images/P/0330484516.01.LZZZZZZZ.jpg',4.6,349,2487),(9780340693179,'Legacy of Silence','Belva Plain',1998,'Bantam Dell Pub Group','http://images.amazon.com/images/P/0385316895.01.LZZZZZZZ.jpg',4.7,299,4274),(9780340836446,'The Alibi','Sandra Brown',2000,'Warner Books','http://images.amazon.com/images/P/0446608653.01.LZZZZZZZ.jpg',3.7,349,1822),(9780345311399,'Private Screening','Richard North Patterson',1994,'Ballantine Books','http://images.amazon.com/images/P/0345311396.01.LZZZZZZZ.jpg',4.7,399,1771),(9780345336989,'Nightmare (Xanth Novels (Paperback))','Piers Anthony',1990,'Del Rey Books','http://images.amazon.com/images/P/0345354931.01.LZZZZZZZ.jpg',4.8,299,3315),(9780345360502,'The Angelic Darkness','Richard Zimler',1999,'Arcadia Books','http://images.amazon.com/images/P/1900850303.01.LZZZZZZZ.jpg',4.8,399,4957),(9780345402875,'Airframe','Michael Crichton',1997,'Ballantine Books','http://images.amazon.com/images/P/0345402871.01.LZZZZZZZ.jpg',4.3,199,1355),(9780345404794,'Protect and Defend','Richard North Patterson',2001,'Ballantine Books','http://images.amazon.com/images/P/0345404793.01.LZZZZZZZ.jpg',4.6,399,2994),(9780345465085,'Seabiscuit','Laura Hillenbrand',2003,'Ballantine Books','http://images.amazon.com/images/P/0345465083.01.LZZZZZZZ.jpg',4.6,299,3248),(9780345490643,'Manhattan Hunt Club','John Saul',2002,'Ballantine Books','http://images.amazon.com/images/P/0449006522.01.LZZZZZZZ.jpg',4.6,249,3585),(9780349727806,'Night Watch','Terry Pratchett',2002,'HarperCollins','http://images.amazon.com/images/P/0060013117.01.LZZZZZZZ.jpg',4.6,399,4195),(9780374234577,'PLEADING GUILTY','Scott Turow',1993,'Audioworks','http://images.amazon.com/images/P/0671870432.01.LZZZZZZZ.jpg',4.8,249,4861),(9780375500763,'Care Packages : Letters to Christopher Reeve from Strangers and Other Friends','Dana Reeve',1999,'Random House','http://images.amazon.com/images/P/0375500766.01.LZZZZZZZ.jpg',4.8,199,975),(9780375705854,'Plainsong (Vintage Contemporaries)','Kent Haruf',2000,'Vintage','http://images.amazon.com/images/P/0375705856.01.LZZZZZZZ.jpg',3.7,349,1617),(9780375724374,'Anil\'s Ghost','Michael Ondaatje',2000,'Knopf','http://images.amazon.com/images/P/0375410538.01.LZZZZZZZ.jpg',3.7,299,1076),(9780375751516,'The Picture of Dorian Gray (Modern Library (Paperback))','Oscar Wilde',1998,'Modern Library','http://images.amazon.com/images/P/0375751513.01.LZZZZZZZ.jpg',4.7,199,2147),(9780375759772,'Prague : A Novel','Arthur Phillips',2003,'Random House Trade Paperbacks','http://images.amazon.com/images/P/0375759778.01.LZZZZZZZ.jpg',4.6,349,885),(9780375801532,'The Iron Giant','Ted Hughes',1999,'Knopf Books for Young Readers','http://images.amazon.com/images/P/0375801677.01.LZZZZZZZ.jpg',4.8,349,2985),(9780380766550,'The Elusive Flame','Kathleen E. Woodiwiss',1999,'Avon','http://images.amazon.com/images/P/0380807866.01.LZZZZZZZ.jpg',4.8,349,3315),(9780385033626,'Bless The Beasts And Children : Bless The Beasts And Children','Glendon Swarthout',1995,'Pocket','http://images.amazon.com/images/P/0671521519.01.LZZZZZZZ.jpg',4.3,349,677),(9780385182447,'Pet Sematary','Stephen King',1994,'Signet Book','http://images.amazon.com/images/P/0451162072.01.LZZZZZZZ.jpg',4.7,299,1263),(9780385336772,'Diary of a Mad Mom-To-Be','Laura Wolf',2003,'Delta','http://images.amazon.com/images/P/0385336772.01.LZZZZZZZ.jpg',4.6,299,1355),(9780385493802,'The Testament','John Grisham',1999,'Dell','http://images.amazon.com/images/P/0440234743.01.LZZZZZZZ.jpg',4.8,199,4546),(9780385511612,'Bleachers','John Grisham',2003,'Doubleday','http://images.amazon.com/images/P/0385511612.01.LZZZZZZZ.jpg',4.6,199,352),(9780385735766,'Sisterhood of the Traveling Pants','Ann Brashares',2003,'Delacorte Books for Young Readers','http://images.amazon.com/images/P/0385730586.01.LZZZZZZZ.jpg',4.6,299,3033),(9780393045215,'The Mummies of Urumchi','E. J. W. Barber',1999,'W. W. Norton &amp; Company','http://images.amazon.com/images/P/0393045218.01.LZZZZZZZ.jpg',4.8,399,1433),(9780393323528,'Next: The Future Just Happened','Michael Lewis',2001,'W.W. Norton &amp; Company','http://images.amazon.com/images/P/0393020371.01.LZZZZZZZ.jpg',4.6,399,4106),(9780394513928,'Congo','Michael Crichton',1995,'Ballantine Books','http://images.amazon.com/images/P/0345378490.01.LZZZZZZZ.jpg',4.3,249,1260),(9780394586236,'Possession: A Romance','A. S. Byatt',1990,'Random House Inc','http://images.amazon.com/images/P/0394586239.01.LZZZZZZZ.jpg',4.8,399,4846),(9780399134203,'The Joy Luck Club','Amy Tan',1994,'Prentice Hall (K-12)','http://images.amazon.com/images/P/0804106304.01.LZZZZZZZ.jpg',4.7,199,788),(9780399138683,'The Cat Who Came to Breakfast (Cat Who... (Hardcover))','Lilian Jackson Braun',1994,'Putnam Pub Group','http://images.amazon.com/images/P/0399138684.01.LZZZZZZZ.jpg',4.7,299,112),(9780399145766,'What If?: The World\'s Foremost Military Historians Imagine What Might Have Been','Robert Cowley',2000,'Berkley Publishing Group','http://images.amazon.com/images/P/0425176428.01.LZZZZZZZ.jpg',3.7,399,259),(9780425133545,'The Sum of All Fears','Tom Clancy',2002,'Berkley Publishing Group','http://images.amazon.com/images/P/0425184226.01.LZZZZZZZ.jpg',4.6,299,2992),(9780425163092,'Chocolate Jesus','Stephan Jaramillo',1998,'Berkley Publishing Group','http://images.amazon.com/images/P/0425163091.01.LZZZZZZZ.jpg',4.7,199,770),(9780425164402,'Only Love (Magical Love)','Erich Segal',1998,'Berkley Publishing Group','http://images.amazon.com/images/P/0425164403.01.LZZZZZZZ.jpg',4.7,349,3514),(9780435272685,'Great Expectations (Heinemann Guided Readers)','John Milne',1995,'Delta Systems','http://images.amazon.com/images/P/0435272683.01.LZZZZZZZ.jpg',4.3,399,2697),(9780439064866,'Harry Potter and the Chamber of Secrets','J.K. Rowling',1998,'Scholastic','https://m.media-amazon.com/images/I/91WqeCn-PxL._SL1500_.jpg',4.7,300,6200),(9780439095020,'Tell Me This Isn\'t Happening','Robynn Clairday',1999,'Scholastic','http://images.amazon.com/images/P/0439095026.01.LZZZZZZZ.jpg',4.8,349,4506),(9780439136365,'Harry Potter and the Prisoner of Azkaban','J.K. Rowling',1999,'Scholastic','https://m.media-amazon.com/images/I/A1D9WdGRYzL._SL1500_.jpg',4.9,300,6800),(9780439139595,'Harry Potter and the Goblet of Fire','J.K. Rowling',2000,'Scholastic','https://m.media-amazon.com/images/I/91SI2owt1XL._SL1500_.jpg',4.8,375,7000),(9780439358071,'Harry Potter and the Order of the Phoenix','J.K. Rowling',2003,'Scholastic','https://m.media-amazon.com/images/I/91TzeItvNFL._SL1500_.jpg',4.6,375,6700),(9780439784542,'Harry Potter and the Half-Blood Prince','J.K. Rowling',2005,'Scholastic','https://m.media-amazon.com/images/I/91g0m3EGvpL._SL1500_.jpg',4.7,375,6900),(9780440337669,'This Year It Will Be Different: And Other Stories','Maeve Binchy',1997,'Dell','http://images.amazon.com/images/P/0440223571.01.LZZZZZZZ.jpg',4.3,299,3690),(9780440949428,'Locked in Time (Laurel Leaf Books)','Lois Duncan',1986,'Laure Leaf','http://images.amazon.com/images/P/0440949424.01.LZZZZZZZ.jpg',4.8,199,3684),(9780446527163,'Wish You Well','David Baldacci',2000,'Warner Books','http://images.amazon.com/images/P/0446527165.01.LZZZZZZZ.jpg',3.7,249,1954),(9780446529785,'A Kiss Remembered','Sandra Brown',2003,'Warner Books','http://images.amazon.com/images/P/0446612618.01.LZZZZZZZ.jpg',4.6,249,2983),(9780446601641,'Slow Waltz in Cedar Bend','Robert James Waller',1994,'Warner Books','http://images.amazon.com/images/P/0446601640.01.LZZZZZZZ.jpg',4.7,249,3461),(9780446607605,'The Witchfinder (Amos Walker Mystery Series)','Loren D. Estleman',1998,'Brilliance Audio - Trade','http://images.amazon.com/images/P/1567407781.01.LZZZZZZZ.jpg',4.7,349,3343),(9780446610391,'The Rescue','Nicholas Sparks',2001,'Warner Books','http://images.amazon.com/images/P/0446610399.01.LZZZZZZZ.jpg',4.6,199,4787),(9780449005613,'Seabiscuit: An American Legend','Laura Hillenbrand',2002,'Ballantine Books','http://images.amazon.com/images/P/0449005615.01.LZZZZZZZ.jpg',4.6,249,4507),(9780449203910,'Blood Oath','David Morrell',1994,'St. Martin\'s Press','http://images.amazon.com/images/P/0312953453.01.LZZZZZZZ.jpg',4.7,349,3595),(9780449908488,'The Silent Cry (William Monk Novels (Paperback))','Anne Perry',1998,'Ivy Books','http://images.amazon.com/images/P/0804117934.01.LZZZZZZZ.jpg',4.7,199,2072),(9780449911006,'Patty Jane\'s House of Curl (Ballantine Reader\'s Circle)','Lorna Landvik',1996,'Ballantine Books','http://images.amazon.com/images/P/0449911004.01.LZZZZZZZ.jpg',4.3,399,4404),(9780451205193,'Lady in Green/Minor Indiscretions (Signet Regency Romance)','Barbara Metzger',2002,'Signet Book','http://images.amazon.com/images/P/0451205197.01.LZZZZZZZ.jpg',4.6,399,4356),(9780451208088,'The Short Forever','Stuart Woods',2003,'Signet Book','http://images.amazon.com/images/P/0451208080.01.LZZZZZZZ.jpg',4.6,399,4817),(9780451451460,'The Catswold Portal','Shirley Rousseau Murphy',1993,'Roc','http://images.amazon.com/images/P/0451452755.01.LZZZZZZZ.jpg',4.8,199,3492),(9780451529305,'Little Women','Louisa May Alcott',1988,'Signet Classics','https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1562690475i/1934.jpg',4.8,299,532),(9780451530820,'Emma (Signet Classics (Paperback))','Jane Austen',1996,'Signet Classics','http://images.amazon.com/images/P/0451526279.01.LZZZZZZZ.jpg',4.6,299,4319),(9780452264465,'Beloved (Plume Contemporary Fiction)','Toni Morrison',1994,'Plume','http://images.amazon.com/images/P/0452264464.01.LZZZZZZZ.jpg',4.7,349,2264),(9780452282155,'Girl with a Pearl Earring','Tracy Chevalier',2001,'Plume Books','http://images.amazon.com/images/P/0452282152.01.LZZZZZZZ.jpg',4.6,199,1187),(9780452285217,'Lies and the Lying Liars Who Tell Them: A Fair and Balanced Look at the Right','Al Franken',2003,'Dutton Books','http://images.amazon.com/images/P/0525947647.01.LZZZZZZZ.jpg',4.6,249,331),(9780486475707,'Great Expectations (Dover Thrift Editions)','Charles Dickens',2001,'Dover Publications','http://images.amazon.com/images/P/0486415864.01.LZZZZZZZ.jpg',4.6,199,2159),(9780505524997,'Contact','Susan Grant',2002,'Love Spell','http://images.amazon.com/images/P/0505524996.01.LZZZZZZZ.jpg',4.6,349,3362),(9780517705827,'The Brimstone Wedding','Barbara Vine',1997,'Penguin Books Ltd','http://images.amazon.com/images/P/0140252800.01.LZZZZZZZ.jpg',3.7,299,2244),(9780525536291,'The Vanishing Half','Brit Bennett',2020,'Riverhead Books','https://m.media-amazon.com/images/I/71AhaMqMsxL._SL1500_.jpg',4.6,345,7200),(9780525620808,'Mexican Gothic','Silvia Moreno-Garcia',2020,'Del Rey','https://m.media-amazon.com/images/I/91JWQ95s5NL._SL1500_.jpg',4.1,315,6800),(9780545010221,'Harry Potter and the Deathly Hallows','J.K. Rowling',2007,'Scholastic','https://m.media-amazon.com/images/I/91VsRHjTY-L._SL1500_.jpg',4.9,450,7200),(9780545664516,'Born Confused','Tanuja Desai Hidier',2003,'Push','http://images.amazon.com/images/P/0439510112.01.LZZZZZZZ.jpg',4.6,249,4442),(9780552145985,'Jingo: A Discworld Novel (Discworld Series/Terry Pratchett)','Terry Pratchett',1998,'HarperPrism','http://images.amazon.com/images/P/0061050474.01.LZZZZZZZ.jpg',4.7,349,804),(9780552148405,'Thief of Time','Terry Pratchett',2001,'HarperCollins Publishers','http://images.amazon.com/images/P/0060199563.01.LZZZZZZZ.jpg',4.6,249,1820),(9780552171366,'Deception Point','Dan Brown',2002,'Pocket','http://images.amazon.com/images/P/0671027387.01.LZZZZZZZ.jpg',4.6,299,4480),(9780553051278,'McDonald\'s: Behind the Arches','John F. Love',1995,'Bantam','http://images.amazon.com/images/P/0553347594.01.LZZZZZZZ.jpg',4.3,249,4558),(9780553122688,'Getting Well Again','O. Carol Simonton Md',1992,'Bantam','http://images.amazon.com/images/P/0553280333.01.LZZZZZZZ.jpg',4.8,299,1569),(9780553278224,'Martian Chronicles','Ray Bradbury',1997,'William Morrow','http://images.amazon.com/images/P/0380973839.01.LZZZZZZZ.jpg',4.3,349,1844),(9780553584387,'Dead Aim','Iris Johansen',2004,'Bantam Books','http://images.amazon.com/images/P/0553584383.01.LZZZZZZZ.jpg',4.6,249,928),(9780571364879,'Klara and the Sun','Kazuo Ishiguro',2021,'Faber & Faber','https://m.media-amazon.com/images/I/71r5mud+JCL._SL1500_.jpg',4.1,330,6600),(9780571365449,'Beautiful World, Where Are You','Sally Rooney',2021,'Faber & Faber','https://m.media-amazon.com/images/I/81o1NMoKErL._SL1500_.jpg',4.0,330,6800),(9780575068858,'The Last Hero : A Discworld Fable (Discworld Novels (Hardcover))','Terry Pratchett',2001,'HarperCollins','http://images.amazon.com/images/P/0061040967.01.LZZZZZZZ.jpg',4.6,299,1324),(9780590629713,'Clifford\'s Sports Day','Norman Bridwell',1996,'Scholastic','http://images.amazon.com/images/P/0590629719.01.LZZZZZZZ.jpg',4.3,249,2635),(9780593135228,'Project Hail Mary','Andy Weir',2021,'Ballantine Books','https://m.media-amazon.com/images/I/91Gws4BuelL._SL1500_.jpg',4.7,405,8300),(9780593311929,'A Judgement in Stone','Ruth Rendell',2000,'Vintage Books USA','http://images.amazon.com/images/P/0375704965.01.LZZZZZZZ.jpg',3.7,249,312),(9780609804612,'Our Dumb Century: The Onion Presents 100 Years of Headlines from America\'s Finest News Source','The Onion',1999,'Three Rivers Press','http://images.amazon.com/images/P/0609804618.01.LZZZZZZZ.jpg',4.8,299,389),(9780670035267,'The Green Man : Tales from the Mysthic Forest','Ellen Datlow',2002,'Viking Juvenile','http://images.amazon.com/images/P/0670035262.01.LZZZZZZZ.jpg',4.6,349,4041),(9780671004576,'Before I Say Good-Bye','Mary Higgins Clark',2001,'Pocket','http://images.amazon.com/images/P/0671004573.01.LZZZZZZZ.jpg',4.6,199,4037),(9780671021740,'Eyes On Crime: Hardy Boys #153','Franklin W. Dixon',1998,'Aladdin','http://images.amazon.com/images/P/0671021745.01.LZZZZZZZ.jpg',4.7,299,3063),(9780671027360,'Angels &amp; Demons','Dan Brown',2001,'Pocket Star','http://images.amazon.com/images/P/0671027360.01.LZZZZZZZ.jpg',4.6,299,1817),(9780671047610,'Skin And Bones','Franklin W. Dixon',2000,'Aladdin','http://images.amazon.com/images/P/0671047612.01.LZZZZZZZ.jpg',3.7,299,1305),(9780671864767,'Relics (Star Trek: The Next Generation)','Michael Jan Friedman',1992,'Star Trek','http://images.amazon.com/images/P/0671864769.01.LZZZZZZZ.jpg',4.8,249,314),(9780671888589,'I\'ll Be Seeing You','Mary Higgins Clark',1994,'Pocket','http://images.amazon.com/images/P/0671888587.01.LZZZZZZZ.jpg',4.7,249,4825),(9780679423072,'Nicholas Nickleby (Everyman\'s Library)','Charles Dickens',1993,'Alfred A. Knopf','http://images.amazon.com/images/P/0679423079.01.LZZZZZZZ.jpg',4.8,349,4539),(9780679425601,'Under the Black Flag: The Romance and the Reality of Life Among the Pirates','David Cordingly',1996,'Random House','http://images.amazon.com/images/P/0679425608.01.LZZZZZZZ.jpg',4.3,249,3221),(9780679444817,'Timeline','Michael Crichton',2000,'Ballantine Books','http://images.amazon.com/images/P/0345417623.01.LZZZZZZZ.jpg',3.7,399,904),(9780679751342,'Angels &amp; Insects : Two Novellas','A. S. Byatt',1994,'Vintage','http://images.amazon.com/images/P/0679751343.01.LZZZZZZZ.jpg',4.7,399,2780),(9780679762836,'Midnight in the Garden of Good and Evil: A Savannah Story','John Berendt',1994,'Random House','http://images.amazon.com/images/P/0679429220.01.LZZZZZZZ.jpg',4.7,399,2489),(9780679865698,'Haveli (Laurel Leaf Books)','Suzanne Fisher Staples',1995,'Laurel Leaf','http://images.amazon.com/images/P/0679865691.01.LZZZZZZZ.jpg',4.3,399,3825),(9780684176536,'The Forsyte Saga : The Man of Property and In Chancery','John Galsworthy',2002,'Touchstone','http://images.amazon.com/images/P/0743245024.01.LZZZZZZZ.jpg',4.6,299,3673),(9780684191416,'Postmortem (Kay Scarpetta Mysteries (Paperback))','Patricia Cornwell',1998,'Pocket','http://images.amazon.com/images/P/0671023616.01.LZZZZZZZ.jpg',4.7,399,3201),(9780684192406,'Body of Evidence (Kay Scarpetta Mysteries (Paperback))','Patricia Cornwell',1992,'Avon','http://images.amazon.com/images/P/0380717018.01.LZZZZZZZ.jpg',4.8,199,3495),(9780684820958,'Pretend You Don\'t See Her','Mary Higgins Clark',1998,'Pocket','http://images.amazon.com/images/P/0671867156.01.LZZZZZZZ.jpg',4.7,349,3160),(9780684833392,'Catch 22','Joseph Heller',1996,'Simon &amp; Schuster','http://images.amazon.com/images/P/0684833395.01.LZZZZZZZ.jpg',4.3,349,2655),(9780684848785,'Tis : A Memoir','Frank McCourt',1999,'Scribner','http://images.amazon.com/images/P/0684848783.01.LZZZZZZZ.jpg',4.8,299,3795),(9780688046590,'The Pillars of the Earth','Ken Follett',1996,'Signet Book','http://images.amazon.com/images/P/0451166892.01.LZZZZZZZ.jpg',4.3,199,3105),(9780689821165,'Flood : Mississippi 1927','Kathleen Duey',1998,'Aladdin','http://images.amazon.com/images/P/0689821166.01.LZZZZZZZ.jpg',4.7,299,1012),(9780689862724,'The Girl Who Loved Tom Gordon','Stephen King',2000,'Pocket','http://images.amazon.com/images/P/0671042858.01.LZZZZZZZ.jpg',3.7,399,1949),(9780712679718,'The Street Lawyer','John Grisham',1999,'Dell','http://images.amazon.com/images/P/0440225701.01.LZZZZZZZ.jpg',4.8,199,123),(9780718137625,'The Winter King: A Novel of Arthur (The Warlord Chronicles: I)','Bernard Cornwell',1997,'St. Martin\'s Griffin','http://images.amazon.com/images/P/0312156960.01.LZZZZZZZ.jpg',4.3,399,3552),(9780739405710,'The Tall Pine Polka','Lorna Landvik',1999,'Ballantine Books','http://images.amazon.com/images/P/0345433173.01.LZZZZZZZ.jpg',4.8,299,4972),(9780743203982,'Flu: The Story of the Great Influenza Pandemic of 1918 and the Search for the Virus That Caused It','Gina Bari Kolata',1999,'Farrar Straus Giroux','http://images.amazon.com/images/P/0374157065.01.LZZZZZZZ.jpg',4.8,349,1879),(9780743225700,'Bringing Down the House: The Inside Story of Six M.I.T. Students Who Took Vegas for Millions','Ben Mezrich',2003,'Free Press','http://images.amazon.com/images/P/0743249992.01.LZZZZZZZ.jpg',4.6,399,327),(9780743273565,'The Great Gatsby','F. Scott Fitzgerald',1925,'Charles Scribner\'s Sons','https://m.media-amazon.com/images/I/61PxxqzdJPL._SL1491_.jpg',4.2,180,4700),(9780743403849,'Decipher','Stel Pavlou',2002,'Simon &amp; Schuster (Trade Division)','http://images.amazon.com/images/P/0743403843.01.LZZZZZZZ.jpg',4.6,199,615),(9780743477659,'Turning Thirty','Mike Gayle',2000,'Hodder &amp; Stoughton General Division','http://images.amazon.com/images/P/0340767936.01.LZZZZZZZ.jpg',3.7,349,1846),(9780743491532,'All That Remains (Kay Scarpetta Mysteries (Paperback))','Patricia Cornwell',1993,'Avon','http://images.amazon.com/images/P/0380718332.01.LZZZZZZZ.jpg',4.8,349,2079),(9780747266808,'From the Corner of His Eye','Dean Koontz',2001,'Bantam Books','http://images.amazon.com/images/P/0553582747.01.LZZZZZZZ.jpg',4.6,249,2471),(9780747532743,'Harry Potter and the Philosopher\'s Stone','J.K. Rowling',1997,'Bloomsbury','https://m.media-amazon.com/images/I/91A6EgLH+2L._SL1500_.jpg',4.8,300,6500),(9780747557401,'Lying Awake','Mark Salzman',2000,'Alfred A. Knopf','http://images.amazon.com/images/P/0375406328.01.LZZZZZZZ.jpg',3.7,199,1468),(9780749748029,'The Folk of the Faraway Tree','Enid Blyton',2002,'Egmont Childrens Books','http://images.amazon.com/images/P/0749748028.01.LZZZZZZZ.jpg',4.6,349,1887),(9780755331611,'Wicked: The Life and Times of the Wicked Witch of the West','Gregory Maguire',1996,'Regan Books','http://images.amazon.com/images/P/0060987103.01.LZZZZZZZ.jpg',4.3,399,1938),(9780755349340,'Roses Are Red (Alex Cross Novel)','James Patterson',2001,'Warner Vision','http://images.amazon.com/images/P/0446605484.01.LZZZZZZZ.jpg',4.6,199,1441),(9780759527249,'The Beach House','James Patterson',2003,'Warner Books','http://images.amazon.com/images/P/0446612545.01.LZZZZZZZ.jpg',4.6,349,3469),(9780771074677,'Nights Below Station Street','David Adams Richards',1988,'Emblem Editions','http://images.amazon.com/images/P/0771074670.01.LZZZZZZZ.jpg',4.8,299,3530),(9780786224685,'Left Behind: A Novel of the Earth\'s Last Days (Left Behind #1)','Tim Lahaye',2000,'Tyndale House Publishers','http://images.amazon.com/images/P/0842342702.01.LZZZZZZZ.jpg',3.7,299,2317),(9780802142597,'Silent Snow','Steve Thayer',2000,'Signet Book','http://images.amazon.com/images/P/0451186648.01.LZZZZZZZ.jpg',3.7,349,1734),(9780812575484,'Through Wolf\'s Eyes (Wolf)','Jane Lindskold',2002,'Tor Fantasy','http://images.amazon.com/images/P/0812575482.01.LZZZZZZZ.jpg',4.6,399,2266),(9780814766934,'Female Intelligence','Jane Heller',2001,'St. Martin\'s Press','http://images.amazon.com/images/P/0312261594.01.LZZZZZZZ.jpg',4.6,249,1678),(9780817311452,'Goodbye to the Buttermilk Sky','Julia Oliver',1994,'River City Pub','http://images.amazon.com/images/P/1881320189.01.LZZZZZZZ.jpg',4.7,399,3061),(9780830713547,'Always Daddy\'s Girl: Understanding Your Father\'s Impact on Who You Are','H. Norman Wright',1989,'Regal Books','http://images.amazon.com/images/P/0830714014.01.LZZZZZZZ.jpg',4.8,199,4408),(9780833551542,'Shabanu: Daughter of the Wind (Border Trilogy)','Suzanne Fisher Staples',1991,'Laurel Leaf','http://images.amazon.com/images/P/0679810307.01.LZZZZZZZ.jpg',4.8,299,1433),(9780881929669,'Northwest Wines and Wineries','Chuck Hill',1993,'Speed Graphics','http://images.amazon.com/images/P/0961769947.01.LZZZZZZZ.jpg',4.8,399,4842),(9780963094421,'Angels and Visitations: A Miscellany','Neil Gaiman',1993,'Dreamhaven Books','http://images.amazon.com/images/P/0963094424.01.LZZZZZZZ.jpg',4.8,199,4133),(9780964778313,'An Atmosphere of Eternity: Stories of India','David Iglehart',2002,'Sunflower Press','http://images.amazon.com/images/P/0964778319.01.LZZZZZZZ.jpg',4.6,299,1140),(9780966986105,'Prescription for Terror','Sandra Levy Ceren',1999,'Andrew Scott Publishers','http://images.amazon.com/images/P/0966986105.01.LZZZZZZZ.jpg',4.8,199,3298),(9780971880108,'Wild Animus','Rich Shapero',2004,'Too Far','http://images.amazon.com/images/P/0971880107.01.LZZZZZZZ.jpg',4.6,349,3070),(9780978929701,'The Adventures of Drew and Ellie: The Magical Dress','Charles Noland',2003,'1stBooks Library','http://images.amazon.com/images/P/1414035004.01.LZZZZZZZ.jpg',4.6,349,458),(9780999660201,'Pen Pals','Olivia Goldsmith',2002,'Signet Book','http://images.amazon.com/images/P/0451206673.01.LZZZZZZZ.jpg',4.6,349,1577),(9781250178602,'The Four Winds','Kristin Hannah',2021,'St. Martin\'s Press','https://m.media-amazon.com/images/I/81BvTRnoBoL._SL1500_.jpg',4.3,420,7800),(9781250301697,'The Silent Patient','Alex Michaelides',2019,'Celadon Books','https://m.media-amazon.com/images/I/81JJPDNlxSL._SL1500_.jpg',4.3,300,7400),(9781380204103,'Out Of The Silent Planet','C.S. Lewis',1996,'Scribner','http://images.amazon.com/images/P/0684823802.01.LZZZZZZZ.jpg',4.3,249,4826),(9781401204266,'Hush','Anne Frasier',2002,'Onyx Books','http://images.amazon.com/images/P/0451410319.01.LZZZZZZZ.jpg',4.6,349,2310),(9781401308582,'The Five People You Meet in Heaven','Mitch Albom',2003,'Hyperion','http://images.amazon.com/images/P/0786868716.01.LZZZZZZZ.jpg',4.6,349,4351),(9781416524793,'Angels &amp; Demons','Dan Brown',2003,'Atria','http://images.amazon.com/images/P/0743486226.01.LZZZZZZZ.jpg',4.6,199,2096),(9781444959451,'The Enchanted Wood','Enid Blyton',2002,'Egmont Childrens Books','http://images.amazon.com/images/P/0749748001.01.LZZZZZZZ.jpg',4.6,199,3635),(9781451631586,'Creating Wealth : Retire in Ten Years Using Allen\'s Seven Principles of Wealth!','Robert G. Allen',1986,'Fireside','http://images.amazon.com/images/P/0671621009.01.LZZZZZZZ.jpg',4.8,349,4469),(9781451673319,'Fahrenheit 451','Ray Bradbury',1953,'Ballantine Books','https://m.media-amazon.com/images/I/61z7RDG3OIL._SL1500_.jpg',4.1,195,5100),(9781456774929,'Jane Doe','R. J. Kaiser',1999,'Mira Books','http://images.amazon.com/images/P/1552041778.01.LZZZZZZZ.jpg',4.8,199,3078),(9781472154668,'Where the Crawdads Sing','Delia Owens',2018,'G.P. Putnam\'s Sons','https://m.media-amazon.com/images/I/81e+mSqZvnL._SL1500_.jpg',4.7,330,8500),(9781473616110,'Starship Troopers','Robert A. Heinlein',1987,'Ace Books','http://images.amazon.com/images/P/0441783589.01.LZZZZZZZ.jpg',4.8,349,3964),(9781489053053,'Powder and Patch','Georgette Heyer',2004,'Harlequin','http://images.amazon.com/images/P/0373836023.01.LZZZZZZZ.jpg',4.6,349,1325),(9781501124020,'The Shining','Stephen King',1977,'Doubleday','https://m.media-amazon.com/images/I/81zqohMOk-L._SL1500_.jpg',4.5,300,6000),(9781501171352,'The Last Thing He Told Me','Laura Dave',2021,'Simon & Schuster','https://m.media-amazon.com/images/I/810ZaSf03nL._SL1500_.jpg',4.0,375,6900),(9781508706250,'The Deal','Joe Hutsko',2000,'Tor Books (Mm)','http://images.amazon.com/images/P/0812575954.01.LZZZZZZZ.jpg',3.7,199,3242),(9781519425591,'Scarlet Letter','Nathaniel Hawthorne',1993,'Signet Book','http://images.amazon.com/images/P/0451525221.01.LZZZZZZZ.jpg',4.8,399,2183),(9781524763169,'A Promised Land','Barack Obama',2020,'Crown','https://m.media-amazon.com/images/I/91+NBrXG-PL._SL1500_.jpg',4.8,525,9500),(9781524798666,'Malibu Rising','Taylor Jenkins Reid',2021,'Ballantine Books','https://m.media-amazon.com/images/I/91ZKOOJQs3L._SL1500_.jpg',4.3,360,7500),(9781529195392,'Isle of Dogs','Patricia Cornwell',2002,'Berkley Publishing Group','http://images.amazon.com/images/P/0425182908.01.LZZZZZZZ.jpg',4.6,199,754),(9781558534902,'Life\'s Little Instruction Book (Life\'s Little Instruction Books (Paperback))','H. Jackson Brown',1991,'Thomas Nelson','http://images.amazon.com/images/P/1558531025.01.LZZZZZZZ.jpg',4.8,249,4016),(9781558746220,'A Second Chicken Soup for the Woman\'s Soul (Chicken Soup for the Soul Series)','Jack Canfield',1998,'Health Communications','http://images.amazon.com/images/P/1558746218.01.LZZZZZZZ.jpg',4.7,199,2175),(9781568522609,'Decision in Normandy','Carlo D\'Este',1991,'HarperPerennial','http://images.amazon.com/images/P/0060973129.01.LZZZZZZZ.jpg',4.8,299,925),(9781568950587,'All or Nothing (Wheeler Large Print Books)','Elizabeth Adler',2000,'Island','http://images.amazon.com/images/P/0440234964.01.LZZZZZZZ.jpg',3.7,349,2358),(9781575663937,'More Cunning Than Man: A Social History of Rats and Man','Robert Hendrickson',1999,'Kensington Publishing Corp.','http://images.amazon.com/images/P/1575663937.01.LZZZZZZZ.jpg',4.8,249,905),(9781606410462,'Snow Angels','Stewart O\'Nan',1995,'Penguin Books','http://images.amazon.com/images/P/0140250964.01.LZZZZZZZ.jpg',3.7,199,1545),(9781607515739,'Confessions of a Shopaholic','Sophie Kinsella',2003,'Dell','http://images.amazon.com/images/P/0440241413.01.LZZZZZZZ.jpg',4.6,399,3151),(9781623610432,'Chicken Soup for the Woman\'s Soul (Chicken Soup for the Soul Series (Paper))','Jack Canfield',1996,'Health Communications','http://images.amazon.com/images/P/1558744150.01.LZZZZZZZ.jpg',4.3,399,845),(9781644393376,'The Great God Pan','Donna Jo Napoli',2003,'Wendy Lamb Books','http://images.amazon.com/images/P/0385327773.01.LZZZZZZZ.jpg',4.6,199,835),(9781784708214,'The Testaments','Margaret Atwood',2019,'Nan A. Talese','https://m.media-amazon.com/images/I/71wLwi0OucL._SL1500_.jpg',4.5,360,6700),(9781786174390,'Black Beauty (Illustrated Classics)','Anna Sewell',1995,'Landoll','http://images.amazon.com/images/P/1569871213.01.LZZZZZZZ.jpg',4.6,299,187),(9781786892720,'The Midnight Library','Matt Haig',2020,'Canongate Books','https://m.media-amazon.com/images/I/81J6APjwxlL._SL1500_.jpg',4.2,300,7600),(9781803364186,'The Invisible Life of Addie LaRue','V.E. Schwab',2020,'Tor Books','https://m.media-amazon.com/images/I/61aWZmZDUyL._SL1000_.jpg',4.4,390,7100),(9781840110197,'The Wind in the Willows','Kenneth Grahame',1996,'St. Martin\'s Press','http://images.amazon.com/images/P/0312148267.01.LZZZZZZZ.jpg',4.3,399,2431),(9781841674094,'Gangster','Lorenzo Carcaterra',2002,'Fawcett Books','http://images.amazon.com/images/P/0345425294.01.LZZZZZZZ.jpg',4.6,349,537),(9781841721521,'New Vegetarian: Bold and Beautiful Recipes for Every Occasion','Celia Brooks Brown',2001,'Ryland Peters &amp; Small Ltd','http://images.amazon.com/images/P/1841721522.01.LZZZZZZZ.jpg',4.6,199,3963),(9781844080380,'Rebecca','Daphne Du Maurier',1994,'Avon','http://images.amazon.com/images/P/0380778556.01.LZZZZZZZ.jpg',4.7,199,4911),(9781849162883,'The Girl with the Dragon Tattoo','Stieg Larsson',2005,'Norstedts Förlag','https://m.media-amazon.com/images/I/61Qs-hoZ-TL._SL1200_.jpg',4.3,300,5500),(9781850813613,'Pride and Prejudice (Dover Thrift Editions)','Jane Austen',1995,'Dover Publications','http://images.amazon.com/images/P/0486284735.01.LZZZZZZZ.jpg',4.3,299,4144),(9781853260056,'Tess of the D\'Urbervilles (Wordsworth Classics)','Thomas Hardy',1997,'NTC/Contemporary Publishing Company','http://images.amazon.com/images/P/1853260053.01.LZZZZZZZ.jpg',4.6,249,2102),(9781853262401,'Heart of Darkness (Wordsworth Collection)','Joseph Conrad',1998,'NTC/Contemporary Publishing Company','http://images.amazon.com/images/P/1853262404.01.LZZZZZZZ.jpg',4.7,199,3618),(9781879384491,'If I\'d Known Then What I Know Now: Why Not Learn from the Mistakes of Others? : You Can\'t Afford to Make Them All Yourself','J. R. Parrish',2003,'Cypress House','http://images.amazon.com/images/P/1879384493.01.LZZZZZZZ.jpg',4.6,199,1783),(9781936365906,'The Middle Stories','Sheila Heti',2004,'House of Anansi Press','http://images.amazon.com/images/P/0887841740.01.LZZZZZZZ.jpg',4.6,249,3359),(9781982113353,'Icebound','Dean R. Koontz',2000,'Bantam Books','http://images.amazon.com/images/P/0553582909.01.LZZZZZZZ.jpg',3.7,199,668),(9781984806758,'People We Meet on Vacation','Emily Henry',2021,'Berkley','https://m.media-amazon.com/images/I/71YdsKNLPAL._SL1500_.jpg',4.4,285,6300),(9782908964592,'Lieux dits','Michel Tournier',2002,'Gallimard','http://images.amazon.com/images/P/2070423204.01.LZZZZZZZ.jpg',4.6,199,602),(9783060311170,'The Curious Incident of the Dog in the Night-Time : A Novel','Mark Haddon',2003,'Doubleday','http://images.amazon.com/images/P/0385509456.01.LZZZZZZZ.jpg',4.6,199,1243),(9789796943395,'Team Bush : Leadership Lessons from the Bush White House','Donald F. Kettl',2003,'McGraw-Hill','http://images.amazon.com/images/P/0071416331.01.LZZZZZZZ.jpg',4.6,199,161);
/*!40000 ALTER TABLE `books_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-26 15:57:47
