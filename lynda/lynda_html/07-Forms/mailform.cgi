#!/usr/bin/perl
# mailform.cgi
# Copyright (C) 1997-2009 William E. Weinman
#
# generic CGI email generator
# change $malto, $subject, and $sendmail to use
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

# where to send the mail
$mailto = "you\@yourhost.com";

# a default subject line
$subject = "Mailform Response";

# your sendmail location. ask your system administrator.
# or just try this, it works most of the time
$sendmail = "/usr/lib/sendmail -t";

# DON'T MODIFY BELOW THIS LINE
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
$mailfrom = $mailto;
$sendmaildashfokay = 1;
$program = "mailform.cgi";
$version = "1.0";
$byline = "(by Bill Weinman <wew\@bearnet.com>)";

print "content-type: text/html\n\n";
%q = getquery();

$emessage = "$subject:\n\n";
foreach $k (sort keys %q) {
  $emessage .= "$k : $q{$k}\n"
  }
$emessage .= "\n---\n Sent by $program $version $byline\n";
sendmessage();
done();

sub done
{
print <<HERE;
<title> $subject </title>
<body bgcolor=white>

<h1>$subject</h1>

<p> Your message has been sent. 

<pre>
$emessage
</pre>

HERE
}

# sendmessage
#
# sends email to $mailto from $mailfrom
# with $subject and $emessage
#
sub sendmessage
{
$dashf = $sendmaildashfokay ? "-f $mailfrom" : "";
open(SENDMAIL, "|$sendmail $dashf") or die "can't open $sendmail\n";
print SENDMAIL "X-Mailer: $program $version $byline\n";
print SENDMAIL "From: $mailfrom\n";
print SENDMAIL "To: $mailto\n";
print SENDMAIL "Subject: $subject\n";
print SENDMAIL "\n";
print SENDMAIL "$emessage\n";
close SENDMAIL;
}

# getquery
#
# returns hash of CGI query strings
#
sub getquery
{
my $method = $ENV{'REQUEST_METHOD'};
my $query_string, $pair;
my %query_hash;
my $sep = $/;
undef $/;

$query_string = $ENV{'QUERY_STRING'} if $method eq 'GET';
$query_string = <STDIN> if $method eq 'POST';
$/ = $sep;
return undef unless $query_string;

foreach $pair (split(/&/, $query_string)) {
  $pair =~ s/\+/ /g;
  $pair =~ s/%([\da-f]{2})/pack('c',hex($1))/ieg;
  ($_qsname, $_qsvalue) = split(/=/, $pair);
  $query_hash{$_qsname} = $_qsvalue;
  }
return %query_hash;
}

