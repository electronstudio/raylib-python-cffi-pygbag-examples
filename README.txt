Working:

    python3.12 -m pip install pygbag==0.9.1 --user --upgrade
    python3.12 -m pygbag --PYBUILD 3.12 --ume_block 0 --template noctx.tmpl example1

To test with git version:

    python3.12 -m pip install git+https://github.com/pygame-web/pygbag --user --upgrade
    python3.12 -m pygbag --git --PYBUILD 3.12 --ume_block 0 --template noctx.tmpl example1