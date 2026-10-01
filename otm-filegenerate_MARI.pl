#!/usr/bin/perl
use strict;
use warnings;
use Cwd;
print "\n Enter Filename:";
my $filename=<STDIN>;
chomp $filename;
print "\n Enter the total number of subscribers you want to create:";
my $number_of_subscribers=<STDIN>;
chomp $number_of_subscribers;
print "\n Enter File Size in numbers below 10k:";
my $count=<STDIN>;
chomp $count;
my $path="/opt/product/YOGESH/MARISH_7L_RRBS";
my $working_dir=cwd();


my $file_type=1;
my ($iccid,$msisdn,$pin1,$puk1,$pin2,$puk2,$KI,$ADM,$ACC,$ACC2,$primary_imsi,$num_of_local_imsi,$num_of_roam_imsi);
my @local_imsi;
my @roam_imsi;
my $ind;

#my $number_of_subscribers="700000";

sub init_file2
{
$iccid="8944205946665900000";
$msisdn="7525300000";   #Starting MSISDN Number
$pin1="0000";
$puk1="74745480";
$pin2="0000";
$puk2="36125109";
$KI="2DA0201EC064394D18A0C9333003CAF5";
$ADM="88B2812C72DDFA5C";
$ACC="0001";

$num_of_local_imsi="3";
#@local_imsi=("234562522200000","204043784800000","505199100200000","214259100200000","262439100200000","208259100200000","228549100200000","286960900100000");
#@local_imsi=("234562522700000","204043785700000","505199100700000","214259100700000","262439100700000","208259100700000","228549100700000","286960900700000","294562522700000");
#@local_imsi=("234562523200000","204043786200000","505199101200000","214259101200000","262439101200000","208259101200000","228549101200000 ","286960901200000","294562523200000");
@local_imsi=("613021235000000","322351004000000","304091004000000","405061004000000");


#do not give value here for file format 1
$num_of_roam_imsi="1";
@roam_imsi=("294562523200000");
#my $rg="3";
}


sub init_file1
{
$primary_imsi="850211370000000";
$iccid="7525224113790000000";
$msisdn="9876540000";
$pin1="0000";
$puk1="22622000";
$pin2="0000";
$puk2="45235000";
$KI="2DA0201EC099994D18A0C9333003CAF5";
$ADM="88BB992C92DDFA5C";
$ACC="0001";
$ACC2="0020";

$num_of_local_imsi="1";
@local_imsi=("960041032000000");
}


#my $count="500000";            #Number of MSISDN to be generated



#for(my $j=0;$j<3;$j++)
#
sub file2
{
my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime(time);
my $filename=sprintf("%s_%04d_%02d_%02d_%02d_%02d_%02d_%02d.txt",$filename,$year+1900,$mon+1,$mday,$hour,$min,$sec,$ind);
chdir $path;
open(my $fh,">:encoding(UTF-8)",$filename);
my $i=0;
while($i<$count)
{
  print $fh "$iccid $msisdn $pin1 $puk1 $pin2 $puk2 $KI $ADM $ACC";
  for(my $j=0;$j<$num_of_local_imsi;$j++)
  {
    print $fh " $local_imsi[$j]";
    $local_imsi[$j]++;
  }
  for(my $j=0;$j<$num_of_roam_imsi;$j++)
  {
    print $fh " $roam_imsi[$j]";
    $roam_imsi[$j]++;
  }
  if($i!=($count-1))
  {
   print $fh "\r\n";
  }
  $iccid++;
  $msisdn++;
  $puk1++;
  $puk2++;
  $i++;
}
$ind++;
close($fh);
chdir $working_dir;
}

sub file1
{
my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime(time);
my $filename=sprintf("%s_%04d_%02d_%02d_%02d_%02d_%02d_%02d.txt",$filename,$year+1900,$mon+1,$mday,$hour,$min,$sec,$ind);
chdir $path;
open(my $fh,">",$filename);
my $i=0;
while($i<$count)
{
  print $fh "$primary_imsi";
  for(my $j=0;$j<$num_of_local_imsi;$j++)
  {
    print $fh " $local_imsi[$j]";
    $local_imsi[$j]++;
  }
  print $fh " $iccid $msisdn $pin1 $puk1 $pin2 $puk2 $KI $ADM $ACC $ACC2";
  if($i!=($count-1))
  {
   print $fh "\r\n";
  }
  $primary_imsi++;
  $iccid++;
  $msisdn++;
  $puk1++;
  $puk2++;
  $i++;
}
$ind++;
close($fh);
chdir $working_dir;
}


if($file_type==1)
{
  my $j=0;
  $ind=1;
  init_file1();
  while($j<$number_of_subscribers)
  {
    file1();
    $j+=$count;
  }
}
else
{
  my $j=0;
  $ind=1;
  init_file2();
  while($j<$number_of_subscribers)
  {
    file2();
    $j+=$count;
    print $j,"\n";
  }
}
