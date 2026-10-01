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
my $path="/opt/product/YOGESH/IMS_LOAD_SUBS";
my $working_dir=cwd();


my $file_type=1;
my ($iccid,$msisdn,$pin1,$puk1,$pin2,$puk2,$KI,$ADM,$ACC,$ACC2,$primary_imsi,$num_of_local_imsi,$num_of_roam_imsi);
my @local_imsi;
my @roam_imsi;
my $ind;

#my $number_of_subscribers="10000";

sub init_file2
{
$iccid="9311400000443010000";
$msisdn="9212300000";   #Starting MSISDN Number
$pin1="1000";
$puk1="68491000";
$pin2="1000";
$puk2="78481000";
$KI="2DA0201EC064394D18A0C9333003CAF5";
$ADM="GFR56FRT";
$ACC="1010";
$primary_imsi="931230000440000";

$num_of_local_imsi="1";
@local_imsi=("931560000440000");
#@local_imsi=("234562524700000","204043787700000","505199102700000","214259102700000","262439102700000","208259102700000","228549102700000 ","286960902700000");
#@local_imsi=("413021234000000","222351002000000","204091002000000","505061002000000");


#do not give value here for file format 1
$num_of_roam_imsi="1";
@roam_imsi=("762393558030000");
#my $rg="3";
}


sub init_file1
{
$primary_imsi="208250000000000";
$iccid="8933130002083225246";
$msisdn="33111110000";
$pin1="0000";
$puk1="22622000";
$pin2="0000";
$puk2="45235000";
$KI="2DA0201EC099994D18A0C9333003CAF5";
$ADM="88BB992C92DDFA5C";
$ACC="0001";
$ACC2="0020";

$num_of_local_imsi="1";
@local_imsi=("204047474300000");
}


#my $count="10000";            #Number of MSISDN to be generated



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
  $iccid+=10;
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
  $iccid+=10;
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
