# Breacher
This script checks if your password is on a list of breached passwords. This script uses the pwnedpasswords API (https://api.pwnedpasswords.com) and, as a precaution, splits the hash of your password before sending the request.

<h1>Features</h1>
<p>The script also outputs the number of occurences of your password in the list.</p>

<h1>Requirements</h1>
This script requires 3 python libraries:
<ul>
<li>colorama</li>
<li>requests</li>
<li>hashlib</li>
</ul>

Run "pip install library" to install these libraries.
