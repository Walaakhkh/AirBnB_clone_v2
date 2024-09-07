# 101-setup_web_static.pp

# Ensure Nginx is installed and running
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => Package['nginx'],
}

# Create the necessary directories with appropriate permissions
file { '/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

file { '/data/web_static/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

file { '/data/web_static/releases/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

file { '/data/web_static/shared/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

file { '/data/web_static/releases/test/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

# Create the index.html file in the test folder
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create the symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  force  => true,
}

# Ensure proper ownership and permissions for the entire /data/ directory
file { '/data/':
  recurse => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

# Configure Nginx to serve the content of /data/web_static/current/ at the URL /hbnb_static
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Nginx template for serving the web static content
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}
