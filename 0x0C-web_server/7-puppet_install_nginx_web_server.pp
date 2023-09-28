# Define a package resource to install nginx
package { 'nginx':
  ensure => 'installed',
}

# Define an exec resource to configure Nginx
exec { 'configure_nginx':
  command => 'sudo apt-get update ; sudo apt-get -y install nginx',
  unless  => 'grep "location /redirect_me" /etc/nginx/sites-available/default',
}

# Define an exec resource to create the index.html file with content "Hello World!"
exec { 'create_index_html':
  command => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  unless  => 'grep "Hello World!" /var/www/html/index.html',
}

# Define an exec resource to configure the redirect
exec { 'configure_redirect':
  command => 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/oluwaseundasilva.hashnode.dev\/;\\n\\t}/" /etc/nginx/sites-available/default',
  unless  => 'grep "location /redirect_me" /etc/nginx/sites-available/default',
}

# Define an exec resource to restart nginx
exec { 'restart_nginx':
  command     => 'sudo service nginx restart',
  refreshonly => true,
}

# Notify the restart_nginx exec when any of the configuration changes
notify { 'Restart Nginx':
  subscribe => [Exec['configure_nginx'], Exec['create_index_html'], Exec['configure_redirect']],
  notify    => Exec['restart_nginx'],
}
