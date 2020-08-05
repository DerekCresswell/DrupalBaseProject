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

Information on the technologies used here can be found in the [technologies](#technologies) section.

## Usage

You can copy this template two ways.

1. Fancy
    * On GitHub, press the "Use this template" button.

2. Old school
    * Clone the repo and run `rm -r path/to/repo/.git`.

3. Composer
    * Using Composer, you can create a project with the command `composer create-project derekcresswell/drupalbaseproject`.

After you have the repo cloned follow these instructions to get your site set up :

1. Find and replace "SITE-NAME", "PROJECT-NAME", and "THEME-NAME" with the appropriate names.
    * Also change the `name` at the top of the Lando file.

2. Navigate to the project root and run `inv setup`. This should start your site and set up things like settings.
    * In this file this is a skeleton command for updating the data base on your site. This will need to be filled in manually.

3. Navigate to `web/sites/default/settings.php` and all the way at the button uncomment the last three lines :

```php
if (file_exists($app_root . '/' . $site_path . '/settings.local.php')) {
  include $app_root . '/' . $site_path . '/settings.local.php';
}
```

4. Then you can go to `composer.json` and remove the top few lines (the lines above the `repositories` key).
    * These lines contain information for [Packagist](https://packagist.org/) and do not need to be used in a site.

Then navigate to the site using the links that lando has given you, `site-name.lndo.site`, and finish the set up by following the installation instructions from Drupal.

This should give you a running Drupal site to work on.

### Theme Set Up

For info on setting up a custom theme see the [custom theme base](./web/themes/custom/THEME-NAME/Readme.md).

## Technologies

There are two main technologies used to make the development process a breeze. Installation instructions can be found on their respective websites.

* [Lando](https://lando.dev/)

    > Lando vastly simplifies local development and DevOps so you can focus on what's important; delivering value to your clients and customers.

* [Invoke](http://www.pyinvoke.org/)

    > Invoke is a Python (2.7 and 3.4+) task execution tool & library, drawing inspiration from various sources to arrive at a powerful & clean feature set.

These are the only two dependencies required to fully utilise this repository. Other technologies are used prominently though they are included within Lando.
