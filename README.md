# Drop to Islandora

A proof of concept application for a headless Islandora. Provides a desktop shortcut for Ubuntu that lets users drop a file into Islandora.


## Requirements

* Works on Ubuntu 18.04, not sure whether it works on other Linux distros.
* Python 3 or higher
   * The [Requests](https://2.python-requests.org/en/master/) library
* An [Islandora 8](https://islandora.ca/) repository with the [JSON:API](https://www.drupal.org/project/jsonapi) module installed and enabled (included starting with Drupal 8.7).
   * Drupal's REST API must have "basic" authentication enabled (it is on by default for JSON:API)

## Installation

* `git clone https://github.com/mjordan/droptoislandora.git`

## Usage

### Preparing your desktop shortcut

1. Place the `dragndrop.desktop` file in your Desktop folder.
1. Right click on the shortcut icon, and go to the "Properties" item.
  1. Adjust the path in the "Command" field so it points to your copy of `droptoislandora.py`.
  1. Go to the "Permissions" tab and check "Allow executing file as a program".


### Preparing your Python script

Change the config variables at the top of the `droptoislandora.py` script to match your environment.

### Dragging files up to Islandora

At this point, everything should be ready. If you drag and drop a file onto the desktop icon:

![Drop to Islandora icon](icon.png)

your file will be ingested into Islandora and you will see a notification indicating its URL:

![Notification indicating URL](notification.png)


## Contributing

Bug reports, improvements, feature requests, and PRs welcome. Before you open a pull request, please open an issue.

## License

The Unlicense.
