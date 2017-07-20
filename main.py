from simpleWebSpider import *


def main():
	newSpider = Spider()
	print("Please read README.txt before using this program\n")
	while True:
		print("="*20 + "")
		print("1/ Input target URL")
		print("2/ Input XPath string")
		print("3/ Get XPath result")
		print("4/ Exit")
		print("="*20 + "")
		cmd = int(input("==>> "))
		if cmd not in range(1,5):
			continue
		if cmd == 4:
			break
		elif cmd == 1:
			inputUrl = str(input("Input target URL: "))
			newSpider.GetTargetUrl(inputUrl)
		elif cmd == 2:
			inputXpath = str(input("Input XPath Name: "))
			newSpider.GetXPath(inputXpath)
		elif cmd == 3:
			newSpider.DisplayResult()

main()