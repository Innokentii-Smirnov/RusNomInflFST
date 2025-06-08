# Install dependencies
Currently, requires XFST since the "turn stack" operator works in an unexpected way in Foma.
When this is corrected or we replace "turn stack" with other code,
the application may work with Foma, which can be installed as follows:
```bash
apt install foma
```
Please use your system's packet manager (e. g. brew) in place of apt if necessary.
You can also download a binary from https://fomafst.github.io/
# Run
```bash
./run_all.sh
```
Assuming XFST is installed in the immediately containing directory of this repository.
# Result
The final lexical transducer is the file "Morphonology/ConvToOrth/ConvToOrth.bin". 
