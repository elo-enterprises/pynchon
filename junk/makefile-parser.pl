use MDOM::Document; use MDOM::Dumper; use MDOM::Document::Gmake;
my $dom = MDOM::Document::Gmake->new('Makefile');

# Load a document
# Create the dumper
# Dump the document
#my $Module = MDOM::Document->new( 'Makefile' );
my $Dumper = MDOM::Dumper->new( $dom );
$Dumper->print;
