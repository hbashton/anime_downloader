import itertools, os, sys
from anime_downloader import get_anime_class


def main():
    if len(sys.argv) == 2:
        link = sys.argv[1]
    elif len(sys.argv) >= 3:
        link = sys.argv[1]
        quality = sys.argv[2]
    else:
        link = input("Enter the link of the anime you would like to download: ")
        quality = input("Quality ['360p', '480p', '720p']? ")

    if not quality:
        quality = '720p'

    NineAnime = get_anime_class(link)
    Anime = NineAnime(link, quality=quality)

    print(Anime.title)
    makemydir(Anime.title)

    if sys.argv[3]:
        episodes = sys.argv[3]
    else:
        episodes = input("There are " + str(len(Anime)) + " total episodes. What episodes? [0-100,101,102,103-200]: ")

    ep_range_list = list()
    ep_single_list = list()
    if ',' in episodes:
        episodes_arr = episodes.split(',')
        episodes_arr = [ x.strip() for x in episodes_arr ]

        for i in episodes_arr:
            if '-' in i:
                eprange = i.split('-')
                ep_range_list.append(eprange)
            else:
                ep_single_list.append(int(i))
    else:
        if '-' in episodes:
            ep_range_list.append(episodes.split('-'))
        else:
            ep_single_list.append(int(episodes))

    if ep_range_list:
        for ep_range in ep_range_list:
            ep_range[0] = int(ep_range[0])
            ep_range[1] = int(ep_range[1])
                
            for epnum in range(ep_range[0],ep_range[1] + 1):
                print()
                print("Downloading episode " + str(epnum))
                ep = Anime[epnum - 1]
                ep.download()


    if ep_single_list:
        ep_single_list = [ int(x) for x in ep_single_list ]
        for epnum in ep_single_list:
            print()
            print("Downloading episode " + str(epnum))
            ep = Anime[epnum - 1]
            ep.download()


def makemydir(whatever):
  try:
    os.makedirs(whatever)
  except OSError:
    pass
  # let exception propagate if we just can't
  # cd into the specified directory
  os.chdir(whatever)

if __name__ == '__main__':
    main()
