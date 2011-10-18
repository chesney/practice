#!/usr/bin/perl
# Copyright (C) 1995-2009 William E. Weinman
#
# generic CGI test program
# submit any form, get back a list of variables
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#

use strict;
use CGI;

my $q = new CGI;
my $qvars = $q->Vars;

print "content-type: text/plain\n\n";

print "\n";
print "Please use the mailform.cgi file\n";
print "from the CD and install it on\n";
print "your own server.\n\n";

if(keys %$qvars) {
  print "\n";
  print "CGI Values:\n=================\n";

  for my $k (sort keys %$qvars) {
    print "$k [$qvars->{$k}]\n";
    }
  print "\n";
  }

print "Environment Variables:\n=================\n";

for my $k (sort keys %ENV) {
  print "$k [$ENV{$k}]\n";
  }
print "\n";

print "\n=====\nCopyright 1995-2009 William E. Weinman\n";

