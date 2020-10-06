from instapy import InstaPy

with open('instabot.config') as f:
	credentials = [line.rstrip() for line in f]
#credentials = [x.strip() for x in credentials]

session = InstaPy(username=credentials[0], password=credentials[1])
session.login()
session.like_by_tags(["cyberpunk2077"])
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!"])
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)


session.end()
