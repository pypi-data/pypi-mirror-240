Load commonly used test logic
  $ . "$TESTDIR/testutil"

  $ git init --bare -q repo.git
  $ git init --bare -q repo2.git

  $ hg clone repo.git hgrepo
  updating to branch default
  0 files updated, 0 files merged, 0 files removed, 0 files unresolved
  $ cd hgrepo
  $ hg bookmark -q master
  $ echo thefile > thefile
  $ hg add thefile
  $ fn_hg_commit -m 'add the file'
  $ hg tag thetag
  $ hg push
  pushing to $TESTTMP/repo.git
  searching for changes
  adding objects
  added 2 commits with 2 trees and 2 blobs
  adding reference refs/heads/master
  adding reference refs/tags/thetag
  $ hg tag --remove thetag
  $ hg push
  pushing to $TESTTMP/repo.git
  searching for changes
  adding objects
  added 1 commits with 1 trees and 1 blobs
  updating reference refs/heads/master
  $ hg push ../repo2.git
  pushing to ../repo2.git
  searching for changes
  adding objects
  added 3 commits with 3 trees and 3 blobs
  adding reference refs/heads/master
  $ cd ..
