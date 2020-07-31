from invoke import task

@task
def drush(c, command):
  """
  Runs a drush command in from within Lando.
  """
  c.run('lando drush {}'.format(command), pty=True)

@task
def start(c):
  """
  Starts development site.
  """
  c.run('lando start')

@task
def stop(c):
  """
  Stops development site.
  """
  c.run('lando stop')

@task
def update(c):
  """
  Updates the sites database
  """
  # TODO, pull database down. Set this up to match your infrastructure.
  # Download database into a file called database.sql or similar then uncomment
  # the following lines.

  # c.run('lando db-import database.sql')
  # drush(c, 'cim -y')
  drush(c, 'cr')

@task(
  help = {
    'watch': 'Continually compiles SASS.'
  }
)
def sass(c, watch = False):
  """
  Compiles the themes SASS into CSS.
  """
  command = 'sass'
  if watch:
    command += '-watch'

  c.run("""
    lando ssh -s node -c
    'cd /app/web/themes/custom/THEME-NAME &&
    node_modules/gulp/bin/gulp.js {}'
    """.format(command))

@task(
  pre = [start],
  post = [sass, update]
)
def setup(c):
  """
  Sets up files and site for local environment.
  """

  # Set up development settings.
  try:
    c.run('cp web/sites/default/dev.settings.php web/sites/default/settings.local.php')
    c.run('cp web/sites/default/dev.services.yml web/sites/default/services.local.yml')
  except:
    print('Development settings are only copied on the first set up.')

  # Install node dependencies.
  c.run("""
    lando ssh -s node -c
    'cd /app/web/themes/custom/THEME-NAME &&
    npm install'
    """)
