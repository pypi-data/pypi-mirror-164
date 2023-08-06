from tapdata_cli import cli
server = "192.168.1.132:31321"
access_code = "3324cfdf-7d3e-4792-bd32-571638d4562f"
cli.init(server, access_code)
mysql = cli.DataSource("mysql", name="mysql_66ss66")
mysql.host("106.55.169.3:3306").db("INSURANCE").username("TAPDATA").password("Gotapd8!").type("source").props("")
mysql.validate()
# mongo.host("203.195.236.101").port("27017").db("test").user("admin").password("Gotapd8!").props("authSource=admin")
# mongo.validate()  # available -> True, disabled -> False
# mongo.save()  # success -> True, Failure -> False
