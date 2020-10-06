from instapy import InstaPy

session = InstaPy(username="__instapy__", password="UQBu92kXveT8HgK")
session.login()
session.like_by_tags(["cyberpunk2077"])
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!"])
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)


session.end()
