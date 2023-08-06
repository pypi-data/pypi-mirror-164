import pandas as pd
import json
import requests
import imageio
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os 



def nhl_games(season=201920):
  # build the url for Nice time on Ice API
  URL = 'http://www.nicetimeonice.com/api/seasons/{}/games'
  url = URL.format(season)
  # get the games
  games = requests.get(url).json()
  # put into a dataframe
  df = pd.DataFrame(games)
  df.columns = df.columns.str.lower()
  # return
  return(df)

def nhl_parse_pbp(gid='2019020010'):
  # parse a json file from the NHL stats pbp files
  URL = 'http://statsapi.web.nhl.com/api/v1/game/{}/feed/live'
  url = URL.format(gid)
  # get the data
  pbp = requests.get(url).json()
  # filter out some data
  plays = pbp['liveData']['plays']['allPlays']
  # the container
  df = pd.DataFrame()
  # iterate over each entry
  for i, play in enumerate(plays):
    # setup the dataframe row for the event
    pbp = pd.DataFrame({'gid':[gid]})
    
    # ------- result 
    test = 'result'
    if test in play.keys():
      tmp = play[test]
      r = pd.DataFrame([tmp])
      r.columns = test + "_" + r.columns
      r.columns = r.columns.str.lower()
      pbp = pd.concat([pbp, r], axis=1)
      del r
    
    #  ------- coordinates
    test = 'coordinates'
    if test in play.keys():
      tmp = play[test]
      # ensure that there are data
      if len(tmp) > 0:
        c = pd.DataFrame([tmp])
        c.columns = "coords_" + c.columns
        c.columns = c.columns.str.lower()
        pbp = pd.concat([pbp, c], axis=1)
        del c
    
    #  ------- team
    test = 'team'
    if test in play.keys():
      tmp = play[test]
      t = pd.DataFrame([tmp])
      t.columns = test + "_" + t.columns
      t.columns = t.columns.str.lower()
      pbp = pd.concat([pbp, t], axis=1)
      del t
    
    #  ------- players
    test = 'players'
    if test in play.keys():
      tmp = play[test]
      players_df = pd.DataFrame()
      for i, p in enumerate(tmp):
        tmp_p = p['player']
        tmp_pdf = pd.DataFrame([tmp_p])
        tmp_pdf.columns = "player{}_".format(i+1) + tmp_pdf.columns
        tmp_pdf.columns = tmp_pdf.columns.str.lower()
        players_df = pd.concat([players_df, tmp_pdf], axis=1)
      # append the data
      pbp = pd.concat([pbp, players_df], axis=1)
    
    #  ------- about
    test = 'about'
    if test in play.keys():
      tmp = play[test]
      # extract the goals - we want 1 row worth
      goals = pd.DataFrame.from_dict([tmp['goals']])
      goals.columns = "goals_" + goals.columns
      del tmp['goals']
      # the about data
      a = pd.DataFrame([tmp])
      a.columns = test + "_" + a.columns
      a.columns = a.columns.str.lower()
      # combine
      a = pd.concat([a, goals], axis=1)
      pbp = pd.concat([pbp, a], axis=1)
      # remove
      del a
      del goals
    
    # bind to the pbp
    df = df.append(pbp, ignore_index=True)
    
  # return the data
  return(df)

def create_football_field(linenumbers=True,
                          endzones=True,
                          highlight_line=False,
                          highlight_line_number=50,
                          highlighted_name='Line of Scrimmage',
                          fifty_is_los=False,
                          figsize=(12, 6.33)):
    """
    Function that plots the football field for viewing plays.
    Allows for showing or hiding endzones.
    # ADAPTED FROM:  https://www.kaggle.com/robikscube/nfl-big-data-bowl-plotting-player-position
    """
    rect = patches.Rectangle((0, 0), 120, 53.3, linewidth=0.1,
                             edgecolor='r', facecolor='white', zorder=0)

    fig, ax = plt.subplots(1, figsize=figsize)
    ax.add_patch(rect)

    plt.plot([10, 10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80,
              80, 90, 90, 100, 100, 110, 110, 120, 0, 0, 120, 120],
             [0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3,
              53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 53.3, 0, 0, 53.3],
             color='black')
    if fifty_is_los:
        plt.plot([60, 60], [0, 53.3], color='gold')
        plt.text(62, 50, '<- Player Yardline at Snap', color='gold')
    # Endzones
    if endzones:
        ez1 = patches.Rectangle((0, 0), 10, 53.3,
                                linewidth=0.1,
                                edgecolor='r',
                                facecolor='grey',
                                alpha=0.2,
                                zorder=0)
        ez2 = patches.Rectangle((110, 0), 120, 53.3,
                                linewidth=0.1,
                                edgecolor='r',
                                facecolor='grey',
                                alpha=0.2,
                                zorder=0)
        ax.add_patch(ez1)
        ax.add_patch(ez2)
    plt.xlim(0, 120)
    plt.ylim(-5, 58.3)
    plt.axis('off')
    if linenumbers:
        for x in range(20, 110, 10):
            numb = x
            if x > 50:
                numb = 120 - x
            plt.text(x, 5, str(numb - 10),
                     horizontalalignment='center',
                     fontsize=20,  # fontname='Arial',
                     color='black')
            plt.text(x - 0.95, 53.3 - 5, str(numb - 10),
                     horizontalalignment='center',
                     fontsize=20,  # fontname='Arial',
                     color='black', rotation=180)
    if endzones:
        hash_range = range(11, 110)
    else:
        hash_range = range(1, 120)

    for x in hash_range:
        ax.plot([x, x], [0.4, 0.7], color='black')
        ax.plot([x, x], [53.0, 52.5], color='black')
        ax.plot([x, x], [22.91, 23.57], color='black')
        ax.plot([x, x], [29.73, 30.39], color='black')

    if highlight_line:
        hl = highlight_line_number + 10
        plt.plot([hl, hl], [0, 53.3], color='yellow')
        plt.text(hl + 2, 50, '<- {}'.format(highlighted_name),
                 color='yellow')
    return fig, ax

def nfl_plot_frame(play_file, 
              frame=1, 
              homecol="red", 
              awaycol="blue", 
              ballcol="orange",
              xcoord="x",
              ycoord="y",
              show=True, 
              save=False):
  
  assert isinstance(play_file, pd.DataFrame)
  p = play_file.copy()
  p.columns = p.columns.str.lower()
  xcoord = xcoord.lower()
  ycoord = ycoord.lower()

  # TODO: replace the team label with football to help with the plot below

  fig, ax = create_football_field()
  if frame is not None and isinstance(frame, int):
    p = p.loc[p.frameid==frame, :]
    # away team
    p.query("team == 'away'").plot(x=xcoord, y=ycoord, kind='scatter', ax=ax, color=awaycol, s=30, legend='Away')
    # home team
    p.query("team == 'home'").plot(x=xcoord, y=ycoord, kind='scatter', ax=ax, color=homecol, s=30, legend='Home')   
    # football 
    p.query("team == 'football'").plot(x=xcoord, y=ycoord, kind='scatter', ax=ax, color=ballcol, s=30, legend='Football')
    
  # plt.legend()

  if show:
    plt.show() 

  if save:
    FNAME = "0"*10 + str(frame)
    FNAME = FNAME[-10:] + ".png"
    plt.savefig(f"plots/{FNAME}")  

  plt.close()


def nfl_make_gif(p, 
             fname="play.gif", 
             homecol="red", 
             awaycol="blue", 
             ballcol="orange", 
             show=True, 
             save=False):
  """
  Uses plot_play and create_football_field to take a valid play and plot each frame
  and stitch together the gif for the play on the field.
  """

  # isolate the frames for the play
  frames = list(set(p.frameId))

  # ensure that the plots directory exists, if not, create
  if not "plots" in os.listdir():
    os.mkdir("plots")

  # generate the image for each frame
  for frame in frames:
    nfl_plot_frame(p, frame=frame, save=True, show=False)
  
  # assemble into a gif
  filenames = os.listdir("plots/")
  filenames.sort()
  images = []
  
  for filename in filenames:
    images.append(imageio.imread("plots/"+ filename))

  imageio.mimsave(fname, images)


