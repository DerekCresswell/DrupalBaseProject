# Drupal Base Project

This is a repository to get a jump start on creating a Drupal site.

## Features

This template has base files for the following :

* [Composer file](./composer.json)
    * This just has the bare essentials to avoid bloat.
        * Drupal 9.x
        * Drush 10
        * Admin Toolbar

* [Lando file](./.lando.yml)
    * This is used to create the development containers and site.
    * By default, this installs a :
        * Apache appserver
        * Mysql database
        * Node service
    * There is also tooling for :
        * Drush
        * Phpunit
        * npm

* [Tasks file](./tasks.py)
    * This is a list of frequent tasks that can be used to create, update, start, and stop the development site.

* [Gulpfile (in `web/themes`)](./web/themes/custom/THEME-NAME/gulpfile.js)
    * This allows our themes to utilize SCSS in our theme as opposed to vanilla CSS.

* [Development settings (in `web/sites`)](./web/sites/default/dev.settings.php)
    * The settings for a database connections and other development settings.
    * If you use the automatic set up the file is used as local settings so, you will need to ensure the normal settings file includes the local ones.

Information on the technologies used here can be found in the [usage](#technologies) section.

## Usage

You can copy this template two ways.

1. Fancy
    * On GitHub, press the "Use this template" button.

2. Old school
    * Clone the repo and run "rm -r path/to/repo/.git".

### Technologies
