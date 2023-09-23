# Ensure that puppet-lint is installed at version 2.1.1 using the gem provider

package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}