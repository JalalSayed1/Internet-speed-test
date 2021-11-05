import speedtest

test = speedtest.Speedtest()
down = test.download()
up = test.upload()

print(f"Download speed: {round(down/1000/1000, 2)} MB.")
print(f"Upload speed: {round(up/1000/1000, 2)} MB.")


