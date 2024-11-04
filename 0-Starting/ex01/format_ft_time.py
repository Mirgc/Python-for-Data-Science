import datetime

now = datetime.datetime.now()
epoch = datetime.datetime(1970, 1, 1)
seconds_since_epoch = (now - epoch).total_seconds()

print("Seconds since ",epoch.strftime("%B %d, %Y"), " =", f"{seconds_since_epoch:,.4f}", " or ", f"{seconds_since_epoch:.2e}", " in scientific notation")
print(now.strftime("%b %d %Y"))