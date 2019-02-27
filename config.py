db_file=':memory:'
bulk_size = 100
days_of_history = 10

sql_create_statement = "CREATE TABLE IF NOT EXIST `MeteostationsData`(" \
            "`meteostationID` varchar(255) NOT NULL," \
            "`timestamp` int(11) NOT NULL," \
            "`temperature` double DEFAULT NULL," \
            "`pressure` double DEFAULT NULL,"\
            "`humidity` double DEFAULT NULL,"\
            "`wind_max_ms` double DEFAULT NULL,"\
            "`wind_min_ms` double DEFAULT NULL,"\
            "`wind_avg_ms` double DEFAULT NULL,"\
            "`wind_direction` double DEFAULT NULL"\
            ") "\
            " DEFAULT CHARSET = latin1;"

sql_insert_statement = "INSERT INTO `MeteostationsData` (`meteostationID`, " \
                       "`timestamp`, " \
                       "`temperature`," \
                       " `pressure`," \
                       " `humidity`," \
                       " `wind_max_ms`, " \
                       "`wind_min_ms`, " \
                       "`wind_avg_ms`, " \
                       "`wind_direction`) VALUES " \
                       "('1chipru_67', 1530316801, NULL, NULL, NULL, 0, 0, 0, 38.3203125)," \
                       "('PIOUPIOU_307', 1530316802, NULL, NULL, NULL, 1.8055555555556, 0.27777777777778, 0.83333333333333, 45)," \
                       "('PIOUPIOU_331', 1530316802, NULL, NULL, NULL, 1.4583333333333, 0.41666666666667, 1.0416666666667, 337.5)," \
                       "('1chipru_59', 1530316804, NULL, NULL, NULL, 4.9, 2.2, 3.7, 55.546875)," \
                       "('PIOUPIOU_224', 1530316806, NULL, NULL, NULL, 4.0277777777778, 3.1944444444444, 3.6111111111111, 45)," \
                       "('PIOUPIOU_181', 1530316807, NULL, NULL, NULL, 2.4305555555556, 0.76388888888889, 1.5277777777778, 45)," \
                       "('1chipru_a020a62a0d78', 1530316809, NULL, NULL, NULL, 1.7, 1.1, 1.4, 319.21875)," \
                       "('PIOUPIOU_261', 1530316809, NULL, NULL, NULL, 8.0555555555556, 3.0555555555556, 5.5555555555556, 292.5)," \
                       "('PIOUPIOU_148', 1530316810, NULL, NULL, NULL, 10.138888888889, 6.25, 8.4722222222222, 180)," \
                       "('PIOUPIOU_437', 1530316810, NULL, NULL, NULL, 1.5277777777778, 0.069444444444444, 0.625, 180)," \
                       "('PIOUPIOU_258', 1530316811, NULL, NULL, NULL, 0, 0, 0, 270)," \
                       "('PIOUPIOU_531', 1530316811, NULL, NULL, NULL, 0.90277777777778, 0.069444444444444, 0.55555555555556, 247.5)," \
                       "('PIOUPIOU_526', 1530316812, NULL, NULL, NULL, 9.1666666666667, 5.6944444444444, 7.7777777777778, 135)," \
                       "('PIOUPIOU_350', 1530316814, NULL, NULL, NULL, 0.90277777777778, 0.55555555555556, 0.76388888888889, 67.5)," \
                       "('PIOUPIOU_154', 1530316816, NULL, NULL, NULL, 2.6388888888889, 1.9444444444444, 2.2916666666667, 337.5)," \
                       "('PIOUPIOU_622', 1530316816, NULL, NULL, NULL, 0, 0, 0, 299.2)," \
                       "('PIOUPIOU_104', 1530316819, NULL, NULL, NULL, 0, 0, 0, 292.5)," \
                       "('1chipru_49', 1530316820, NULL, NULL, NULL, 6, 3.5, 4.9, 0)," \
                       "('PIOUPIOU_264', 1530316820, NULL, NULL, NULL, 2.2222222222222, 0.41666666666667, 1.3194444444444, 0)," \
                       "('PIOUPIOU_615', 1530316820, NULL, NULL, NULL, 2.8888888888889, 1.1388888888889, 2.1944444444444, 90.1)," \
                       "('1chipru_71', 1530316821, NULL, NULL, NULL, 1.6, 0.8, 1.2, 89.296875)," \
                       "('PIOUPIOU_560', 1530316821, NULL, NULL, NULL, 0, 0, 0, 0)," \
                       "('PIOUPIOU_371', 1530316823, NULL, NULL, NULL, 2.7083333333333, 0, 0.83333333333333, 157.5)," \
                       "('PIOUPIOU_1019', 1530316825, NULL, NULL, NULL, 6.1111111111111, 2.0138888888889, 4.4444444444444, 45)," \
                       "('PIOUPIOU_483', 1530316827, NULL, NULL, NULL, 2.2916666666667, 0, 1.1805555555556, 67.5);"

sql_add_keys_statement = "ALTER TABLE `MeteostationsData`" \
                         "  ADD UNIQUE KEY `meteostationID` (`meteostationID`,`timestamp`)," \
                         "  ADD KEY `timestampIdx` (`timestamp`);" \
                         "COMMIT;"