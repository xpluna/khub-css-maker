########################################
#   KHub CSS Maker - Final Release
#   Written By - xpbliss#5178
########################################
#   Features:
# - Hides ADs, KrunkTV, KrunkNews and Follow Suggestions
# - Auto-export as social_custom.css
# - RGB and HTML CC support
########################################
#   Changelog:
# - Removed Shadow calculator for good
# - Text Colours now support only HTML CC
########################################

# Functions [Count: 2]
def RGB():
	
	continue_func = input('\n' + '*'*40 + '\n\nRGB Levels range from 0 to 256.\nOpacity levels range from 0 [Pure Transparency] to 100 [No Transparency]\n\nIn code rgb(12, 45, 70 / 20):\n\t12 = R Level\n\t45 = G Level\n\t70 = B Level\n\t20 = Opacity Level\n\nPress ENTER to continue.')
	print("\n" + '*'*40 + "\n\nAccent RGB Levels")

	accR = str(input("R -> ")).strip()
	accG = str(input("G -> ")).strip()
	accB = str(input("B -> ")).strip()
	alpha = str(input('Enter Opacity Level -> ')).strip()

	accentCol = 'rgb(' + accR + ' ' + accG + ' ' + accB + ' / ' + alpha + '%)'

	print("\nShadow RGB Levels")

	shaR = str(input("R -> ")).strip()
	shaG = str(input("G -> ")).strip()
	shaB = str(input("B -> ")).strip()
	sAlpha = str(input('Enter Opacity Level -> ')).strip()
	
	shadowCol = 'rgb(' + shaR + ' ' + shaG + ' ' + shaB + ' / ' + sAlpha + '%)'
	
	with open('social_custom.css', 'w') as obj:
		obj.write("#backgroundImage{background-image: url(" + imageLink + ");}\n#leftAdHol{display:none}\n#rightAdHol{display:none}\n#aHolder{display:none}\na{color:" + _textCol_ + "}\n*{color:" + _textCol_ + "}\n.postCFoll{color:" + _textCol_ + "}\n.postSubInfo{color:" + _textCol_ + "}\n.postTime{color:" + _textCol_ + "}\n.krGivFol{color:" + _textCol_ + "}\n.leftMidHolder{color:" + _textCol_ + "}\n.profileTab{color:" + _textCol_ + "}\n.feedTab{background-color:" +  accentCol + ";box-shadow:0 7px 0 0 " +  shadowCol + "}\n.pSt strong{color:" + _textCol_ + "}\n.pTabA{box-shadow:inset 0 -5px " +  shadowCol + "}\n#navTitle{color:" +  shadowCol + "}\n#hubBox{background-color:" +  shadowCol + "}\n.xpBarB{background-color:" +  shadowCol + "}\n.clsXPBarC{background-color:" +  shadowCol + "}\n.socPost{background-color:" +  accentCol + ";box-shadow:0 7px 0 0 " +  shadowCol + "}\n.scrollItem{background-color:" +  accentCol + ";box-shadow:0 7px 0 0 " +  shadowCol + "}\n.scrollItemNew{background-color:" +  accentCol + ";box-shadow:0 7px 0 0 " +  shadowCol + "}\n.profileTabs{background-color:" +  accentCol + "}\n#chatScroller{background-color:" +  accentCol + "}\n#navBar{background-color:" +  accentCol + "}\n.mapListItem{background-color:" +  accentCol + "}\n.terms{color:" +  shadowCol + "}\n.mapListItem2{background-color:" +  shadowCol + "}\n#searchBtn{background-color:" +  shadowCol + "}\n.regionCard{background-color:" + accentCol + ";box-shadow:0 7px 0 0 " + shadowCol + "}\n#itemsListNav>select{background-color:" + accentCol + "}\n#settingsPop{background-color:" + accentCol + "}\n.settName,.settNameSmall{color:" + _textCol_ + "}\ninput:checked+.slider{background-color:" + shadowCol + "}\n.sliderVal{background:" + shadowCol + "}")
		confirm = input("\n" + '*'*40 + "\n\nDone! Press ENTER to exit.")


def HTML():
	accentCol = str(input("\n" + '*'*40 + "\n\nAccent colour code -> ")).strip()
	shadowCol = str(input("Shadow colour code -> ")).strip()
	
	with open('social_custom.css', 'w') as obj:
		obj.write("#backgroundImage{background-image: url(" + imageLink + ");}\n#leftAdHol{display:none}\n#rightAdHol{display:none}\n#aHolder{display:none}\na{color:" + _textCol_ + "}\n*{color:" + _textCol_ + "}\n.postCFoll{color:" + _textCol_ + "}\n.postSubInfo{color:" + _textCol_ + "}\n.postTime{color:" + _textCol_ + "}\n.krGivFol{color:" + _textCol_ + "}\n.leftMidHolder{color:" + _textCol_ + "}\n.profileTab{color:" + _textCol_ + "}\n.feedTab{background-color:" +  accentCol + ";box-shadow:0 7px 0 0 " +  shadowCol + "}\n.pSt strong{color:" + _textCol_ + "}\n.pTabA{box-shadow:inset 0 -5px " +  shadowCol + "}\n#navTitle{color:" +  shadowCol + "}\n#hubBox{background-color:" +  shadowCol + "}\n.xpBarB{background-color:" +  shadowCol + "}\n.clsXPBarC{background-color:" +  shadowCol + "}\n.socPost{background-color:" +  accentCol + ";box-shadow:0 7px 0 0 " +  shadowCol + "}\n.scrollItem{background-color:" +  accentCol + ";box-shadow:0 7px 0 0 " +  shadowCol + "}\n.scrollItemNew{background-color:" +  accentCol + ";box-shadow:0 7px 0 0 " +  shadowCol + "}\n.profileTabs{background-color:" +  accentCol + "}\n#chatScroller{background-color:" +  accentCol + "}\n#navBar{background-color:" +  accentCol + "}\n.mapListItem{background-color:" +  accentCol + "}\n.terms{color:" +  shadowCol + "}\n.mapListItem2{background-color:" +  shadowCol + "}\n#searchBtn{background-color:" +  shadowCol + "}\n.regionCard{background-color:" + accentCol + ";box-shadow:0 7px 0 0 " + shadowCol + "}\n#itemsListNav>select{background-color:" + accentCol + "}\n#settingsPop{background-color:" + accentCol + "}\n.settName,.settNameSmall{color:" + _textCol_ + "}\ninput:checked+.slider{background-color:" + shadowCol + "}\n.sliderVal{background:" + shadowCol + "}")
		confirm = input("\n" + '*'*40 + "\n\nDone! Press ENTER to exit.")

# End

print('KHub CSS - Final Release\n')

imageLink = str(input("Image link: ")).strip()

_textCol_ = str(input("\n" + '*'*40 + "\n\nHTML Codes contain a #. Example - #fe230\n\nText colour code [in HTML only] -> "))

get_response = str(input("\n" + '*'*40 + "\n\nYou should have the colour codes ready with you. Enter response carefully.\n\nResponse expected = 'HTML' or 'RGB'\t-> ")).upper().strip()

if get_response == 'HTML':
	HTML()

elif get_response == 'RGB':
	RGB()
