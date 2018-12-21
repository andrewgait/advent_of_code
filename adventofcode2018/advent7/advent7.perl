#!/opt/perl/bin/perl

use 5.022;
 
use strict; 
use warnings; 
no warnings 'syntax'; 

use experimental 'signatures'; 

my $BASE_TIME = 60; 
my $ELVES = 5;

#
# Read the input
#
my $input = "input"; 
open my $fh, "<", $input or die "Failed to open $input: $!"; 

my %dependencies; 

while (<$fh>) {
    /^Step (?<requirement>\p{Lu}) must be finished before (?#
      )step (?<target>\p{Lu}) can begin\.$/ or die "Failed to parse $_";

    $dependencies {$+ {target}} {$+ {requirement}} = 1;
    $dependencies {$+ {requirement}} ||= {};
}

my %elf; 
my @free_elves = (1 .. $ELVES); 

my $start = time; 

while (%dependencies) {
    #
    # While we have a free worker, and an item 
    # which may be processed, assign a job, and 
    # mark when it's done.
    #
    while (@free_elves) {
        my ($todo) = sort grep {!keys %{$dependencies {$_}}}
                          keys %dependencies;
        last unless $todo;
        #
        # One less free worker
        #
        my $elf = shift @free_elves;
        #
        # Remove it from the set of things to do
        #
        delete $dependencies {$todo};

        my $pid = fork;

        die "Failed to fork: $!" unless defined $pid;

        if (!$pid) {
            #
            # Child;
            #
            printf "%4d: Elf %d starts working on %s\n" =>
                   time - $start, $elf, $todo;
            sleep $BASE_TIME + ord ($todo) - ord ('A') + 1;
            printf "%4d: Elf %d finished working on %s\n" =>
                   time - $start, $elf, $todo;
            exit;
        }
        #
        # Mark who worked on what.
        #
        $elf {$pid} = [$elf => $todo];
    }
    #
    # Wait for elves...
    #
    my $pid = waitpid -1, 0;

    my $done = $elf {$pid} or die "Huh? What did elf $pid do?";

    delete $dependencies {$_} {$$done [1]} for keys %dependencies;
    push @free_elves => $$done [0];
}

my $end = time; 

say "Time to finish: ", $end - $start, "s"; 

__END__
