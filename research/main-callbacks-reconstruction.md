# Main callback reconstruction

The existing AXPJ revision-zero callback reconstruction is now tied to four exact ROM ranges. It covers link processing, callback initialization, two indirect callback dispatches, and callback2/state assignment. Names follow `pret/pokeruby`; addresses, structure offsets, and range hashes come from the verified Japanese ROM.

The C source and map contain no verbatim ROM byte extracts. Sapphire and Ruby are kept as separate evidence even where functions are byte-identical.
