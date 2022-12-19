-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: bookstore
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `author`
--

LOCK TABLES `author` WRITE;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
INSERT INTO `author` VALUES (1,'Aso Shuichi','Tác giả với nhiều tác phẩm nổi tiếng',NULL,'Nhật Bản'),(2,'Takeshi Shudo','Tajiri sinh ngày 28 tháng 8 năm 1965 tại Tokyo đến bán xe cho hãng Nissan và là một nội trợ.Tajiri lớn lên tại Machida, Tokyo, ở thời điểm nơi đây còn là một vùng nông thôn',NULL,'Nhật Bản'),(3,'Trác Nhã','Trác Nhã là Thạc sĩ Tâm lí học trường Đại học Sư phạm Bắc Kinh. Và tất nhiên cô cũng là một tác giả khá nổi tiếng tại Trung Quốc cũng như Việt Nam và một số quốc gia trong khu vực',NULL,'Trung Quốc'),(4,'Minh','1 tác giả nổi tiếng','minhth@gmail.com','Việt Nam'),(5,'Ngô Tất Tố',' là một nhà văn, nhà báo, nhà Nho học, dịch giả và nhà nghiên cứu có ảnh hưởng lớn ở Việt Nam giai đoạn trước 1954.Ngô Tất Tố sinh năm 1893 (mất năm 1954) ở làng Lộc Hà, tổng Hội Phụ, phủ Từ Sơn, Bắc Ninh (nay là thôn Lộc Hà, xã Mai Lâm, huyện Đông Anh, H',NULL,'Việt Nam'),(6,'Helen Aberson','là một tác giả sách thiếu nhi người Mỹ. Aberson-Mayer nổi tiếng với vai trò đồng tác giả câu chuyện truyền cảm hứng cho bộ phim Dumbo năm 1941',NULL,'Mỹ'),(7,'Stephen King','Stephen King (sinh ngày 21 tháng 9 năm 1947) là nhà văn người Mỹ thiên về thể loại kinh dị hoặc giả tưởng rất được tán thưởng khắp thế giới, đặc biệt với mô-típ biến đổi những tình huống căng thẳng bình thường thành hiện tượng khiếp đảm.',NULL,'Mỹ'),(8,'long','1 nhà toán học đã làm nên sách tham khảo này',NULL,'Việt Nam'),(9,'Jeff Kinney','Tác giả với lối kể chuyện hóm hỉnh rất có duyên cùng những bức hình minh hoạ ngộ nghĩnh ',NULL,'Mỹ'),(10,'Thỏ Bảy Màu','',NULL,'Việt Nam');
/*!40000 ALTER TABLE `author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,1,'0306406','Kẻ Siêu Năng Khốn Khổ','Saiki Kusuo là một nhà ngoại cảm bẩm sinh. Nhưng khác với những người khác vui mừng vì có được sức mạnh siêu nhiên, Kusuo lại coi đó như sự bất hạnh nhất thế giới, và cố gắng sống bình thường mặc cho cái sức mạnh phiền nhiễu này','2015',120,15000,'Việt Nam',50,1),(2,2,'0306422','Pokémon Đặc Biệt','Trong thế giới này, những sinh vật sống với khả năng siêu nhiên - Pokemon. Mọi người, được gọi là Nhà huấn luyện Pokemon, huấn luyện Pokemon chiến đấu với Pokemon của các huấn luyện viên khác: ở một mức độ nhất định, các trận chiến Pokemon giống với các c','2016',120,20000,'Việt Nam',50,1),(3,3,'0394844','Khéo Ăn Nói Sẽ Có Được Thiên Hạ','Một trong những kĩ năng quan trọng nhất mà con người cần có trong cuộc sống là giao tiếp. Giao tiếp giúp bạn vận hành tối đa ưu điểm của mình, tiếp thu được nhiều kiến thức, bài học sống từ người xung quanh. Dù bạn có là người hướng nội hay người hướng ng','2017',100,60000,'Việt Nam',50,1),(4,4,'0348515','Hướng dẫn nấu 200 món ăn truyền thống','Cuốn sách đưa 200 công thức nấu ăn truyền thống giúp bạn thỏa sức tìm tòi khám phá những món ăn truyền thống thời xưa','2018',100,40000,'Việt Nam',100,1),(5,5,'0364101','Tắt đèn','Câu chuyện kể về cuộc sống đen tối của chị Dậu nói riêng và của nông dân Việt Nam thời xưa nói chung trước sự bóc lột của bọn thực dân Pháp thối nát ','2019',120,50000,'Việt Nam',50,1),(6,6,'0305884','Dumbo','Một đàn cò mang những em bé bay ngang qua đoàn xiếc thú đang được vận chuyển bằng tàu lửa đến từ \"Winter Quarters\".Bà voi Jumbo, một trong những con voi trong đoàn xiếc, nhận được con của mình là chú voi con luôn bị chọc ghẹo bởi những cô voi khác vì đôi ','2020',50,100000,'Việt Nam',100,1),(7,7,'0305442','The Green Mile','Câu chuyện là hồi ký của Paul Edgecombe, cựu cai ngục ở khu E, hay còn gọi là Green Mile – Dặm Xanh, khu dành cho các tử tù. Vào những năm 1930, khi còn đang làm việc ở Green Mile, ông đã tiếp nhận John Coffey (tên giống một loại đồ uống nhưng đánh vần kh','1998',300,180000,'Việt Nam',50,1),(8,8,'0311584','Phương Pháp Giải Bài Tập Hoá Học 10','Tuyển tập những phương pháp giải những bài tập Hóa học của lớp 10','2015',100,60000,'Việt Nam',100,1),(9,9,'0315484','Nhật Ký Chú Bé Nhút Nhát','Nội dung chủ yếu kể về cuộc sống xoay quanh cậu bé nhân vật chính Greg Heffley cùng những cảm xúc của cậu','2016',120,50000,'Việt Nam',100,1),(10,10,'0374878','Thỏ Bảy Màu Và Những Người Nghĩ Nó Là Bạn','Nội dung? Bạn nghĩ những câu chuyện mất não của thỏ bày màu này có nội dung à.Hãy cùng khám phá những câu chuyện tấu hài trong thế giới mất não này của thỏ bảy màu','2020',150,80000,'Việt Nam',100,1);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `bookauthor`
--

LOCK TABLES `bookauthor` WRITE;
/*!40000 ALTER TABLE `bookauthor` DISABLE KEYS */;
INSERT INTO `bookauthor` VALUES (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10);
/*!40000 ALTER TABLE `bookauthor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `bookitem`
--

LOCK TABLES `bookitem` WRITE;
/*!40000 ALTER TABLE `bookitem` DISABLE KEYS */;
INSERT INTO `bookitem` VALUES (1,20000,5,10,'Saiki Kusuo là một nhà ngoại cảm bẩm sinh. Nhưng khác với những người khác vui mừng vì có được sức mạnh siêu nhiên, Kusuo lại coi đó như sự bất hạnh nhất thế giới, và cố gắng sống bình thường mặc cho cái sức mạnh phiền nhiễu này','https://cdn0.fahasa.com/media/catalog/product/s/a/saiki-kusuo---ke-sieu-nang-khon-kho---tap-17.jpg','Saiki Kusuo - Kẻ Siêu Năng Khốn Khổ','truyện tranh'),(2,25000,10,10,'Trong thế giới này, những sinh vật sống với khả năng siêu nhiên - Pokemon. Mọi người, được gọi là Nhà huấn luyện Pokemon, huấn luyện Pokemon chiến đấu với Pokemon của các huấn luyện viên khác: ở một mức độ nhất định, các trận chiến Pokemon giống với các cuộc thi thể thao. Các trận đánh được tổ chức cho đến khi một trong hai bên không còn khả năng thi đấu. Theo quy định, nhà huấn luyện mạnh mẽ và giàu kinh nghiệm được tôn vinh. Nhân vật chính - nhà huấn luyện Pokemon Satoshi. Cùng với Pikachu là Pokemon đầu tiên của mình chu du khắp thế giới để trở thành Bậc thầy Huấn luyện Pokémon. Cùng với những người bạn của mình trong suốt hành trình đi qua các vùng khác nhau','https://cdn0.fahasa.com/media/catalog/product/i/m/image_195509_1_41009.jpg','Pokémon Đặc Biệt','truyện tranh'),(3,75000,10,10,'Một trong những kĩ năng quan trọng nhất mà con người cần có trong cuộc sống là giao tiếp. Giao tiếp giúp bạn vận hành tối đa ưu điểm của mình, tiếp thu được nhiều kiến thức, bài học sống từ người xung quanh. Dù bạn có là người hướng nội hay người hướng ngoại thì kĩ năng giao tiếp vẫn góp phần lớn tạo nên sự thành công của bạn.','https://cdn0.fahasa.com/media/catalog/product/b/i/bia_26_8_thanh_ly.jpg','Khéo Ăn Nói Sẽ Có Được Thiên Hạ','Sách tâm lý'),(4,50000,5,10,'Cuốn sách đưa 200 công thức nấu ăn truyền thống giúp bạn thỏa sức tìm tòi khám phá những món ăn truyền thống thời xưa','https://metaisach.com/wp-content/uploads/2019/09/sach-day-nau-an-200-mon-an-truyen-thong.jpg','Hướng dẫn nấu 200 món ăn truyền thống','Sách nấu ăn'),(5,60000,10,10,'Câu chuyện kể về cuộc sống đen tối của chị Dậu nói riêng và của nông dân Việt Nam thời xưa nói chung trước sự bóc lột của bọn thực dân Pháp thối nát ','https://images-na.ssl-images-amazon.com/images/I/615LOfeCkvL.jpg','Tắt đèn','Sách Văn học nghệ thuật'),(6,120000,20,10,'Một đàn cò mang những em bé bay ngang qua đoàn xiếc thú đang được vận chuyển bằng tàu lửa đến từ \"Winter Quarters\".Bà voi Jumbo, một trong những con voi trong đoàn xiếc, nhận được con của mình là chú voi con luôn bị chọc ghẹo bởi những cô voi khác vì đôi tai lớn bất thường của mình và họ đặt cho cậu cái tên là \"Dumbo\".Và câu chuyện của cậu bắt đầu từ đây.','https://cdn0.fahasa.com/media/catalog/product/9/7/9781292420394_1.jpg','Dumbo','Sách thiếu nhi'),(7,200000,20,10,'Câu chuyện là hồi ký của Paul Edgecombe, cựu cai ngục ở khu E, hay còn gọi là Green Mile – Dặm Xanh, khu dành cho các tử tù. Vào những năm 1930, khi còn đang làm việc ở Green Mile, ông đã tiếp nhận John Coffey (tên giống một loại đồ uống nhưng đánh vần khác), một tù nhân da đen khổng lồ bị buộc tội đã cưỡng hiếp và giết chết 2 bé gái da trắng và kết án tử. Nhưng cuộc sống của ông và những người xung quanh đã đảo lộn hoàn toàn sau khi phát hiện ra John có một khả năng đặc biệt có thể giúp đỡ người khác, nhưng lại không thể giúp chính mình tránh khỏi việc bước lên ghế điện','https://cdn0.fahasa.com/media/catalog/product/cache/1/thumbnail/400x400/9df78eab33525d08d6e5fb8d27136e95/i/m/image_244718_1_5505.jpg','The Green Mile','Tiểu thuyết '),(8,65000,10,10,'Tuyển tập những phương pháp giải những bài tập Hóa học của lớp 10','https://cdn0.fahasa.com/media/catalog/product/cache/1/thumbnail/400x400/9df78eab33525d08d6e5fb8d27136e95/i/m/image_189173.jpg','Phương Pháp Giải Bài Tập Hoá Học 10','Sách giáo khoa'),(9,55000,10,10,'Nội dung chủ yếu kể về cuộc sống xoay quanh cậu bé nhân vật chính Greg Heffley cùng những cảm xúc của cậu','https://cdn0.fahasa.com/media/catalog/product/cache/1/thumbnail/400x400/9df78eab33525d08d6e5fb8d27136e95/i/m/image_195509_1_20355.jpg','Nhật Ký Chú Bé Nhút Nhát','Sách thiếu nhi'),(10,90000,10,10,'Nội dung? Bạn nghĩ những câu chuyện mất não của thỏ bày màu này có nội dung à.Hãy cùng khám phá những câu chuyện tấu hài trong thế giới mất não này của thỏ bảy màu','https://cdn0.fahasa.com/media/catalog/product/cache/1/thumbnail/400x400/9df78eab33525d08d6e5fb8d27136e95/b/i/bia-thomau_1.jpg','Thỏ Bảy Màu Và Những Người Nghĩ Nó Là Bạn','truyện tranh');
/*!40000 ALTER TABLE `bookitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cartitem`
--

LOCK TABLES `cartitem` WRITE;
/*!40000 ALTER TABLE `cartitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `cartitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `fullname`
--

LOCK TABLES `fullname` WRITE;
/*!40000 ALTER TABLE `fullname` DISABLE KEYS */;
/*!40000 ALTER TABLE `fullname` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `orderitem`
--

LOCK TABLES `orderitem` WRITE;
/*!40000 ALTER TABLE `orderitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `publisher`
--

LOCK TABLES `publisher` WRITE;
/*!40000 ALTER TABLE `publisher` DISABLE KEYS */;
INSERT INTO `publisher` VALUES (1,1,'Nhà Xuất Bản Kim Đồng','Việt Nam'),(2,2,'Nhà Xuất Bản Kim Đồng','Việt Nam'),(3,3,'Nhà Xuất Bản Kim Đồng','Việt Nam'),(4,4,'Nhà Xuất Bản Kim Đồng','Việt Nam'),(5,5,'Nhà Xuất Bản Kim Đồng','Việt Nam'),(6,6,'Nhà Xuất Bản Kim Đồng','Việt Nam'),(7,7,'Nhà Xuất Bản Kim Đồng','Việt Nam'),(8,8,'Nhà Xuất Bản Kim Đồng','Việt Nam'),(9,9,'Nhà Xuất Bản Kim Đồng','Việt Nam'),(10,10,'Nhà Xuất Bản Kim Đồng','Việt Nam');
/*!40000 ALTER TABLE `publisher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `shipment`
--

LOCK TABLES `shipment` WRITE;
/*!40000 ALTER TABLE `shipment` DISABLE KEYS */;
/*!40000 ALTER TABLE `shipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (10000,1);
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'nam ','str','09865503','minh123@gmail.com');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-02 19:04:02
