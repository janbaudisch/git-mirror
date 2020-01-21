# `git-mirror`

> A tool for mirroring a remote git repository to another one.

## Installation

This tool is just a simple script, so the installation should be straightforward.

### Preqrequisites

 - POSIX shell
 - git

### From Source

Download the script.

```
curl -O https://git.sr.ht/~janbaudisch/git-mirror/blob/<version>/git-mirror
```

(Replace `<version>` with the latest version.)

Make sure the script is executable:

```
chmod +x git-mirror
```

Move it to the bindir:

```
sudo mv git-mirror /usr/bin/git-mirror
```

### Packages

I maintain a [copr repo][copr-url] for Fedora and EPEL.

## Usage

For details, see the manual page for `git-mirror(1)` or `git-mirror help`

There are two commands `setup` and `update`.

### `setup`

Creates a directory used for fetching and pushing to and from the repositories.

Automatically runs `update` to acutally mirror the repository.

```
git-mirror setup path/to/directory https://someserver.domain/user/tomirror git@someserver.domain/user/mirror
```

### `update`

Fetches everything from the primary repository and then pushes it to the mirror.

```
git-mirror update path/to/directory
```

## Example Usage

### 1. Setup

Set up a new mirror directory.

```
git-mirror setup /var/data/some-mirror https://someserver.domain/user/tomirror git@someserver.domain/user/mirror
```

### 2. Cronjob

Add a cronjob (e.g. with `crontab -e`) containing the following:

```
*/5 * * * * git-mirror update /var/data/some-mirror
```

This will update the mirror every 5 minutes.

## In Action

This code mirrors itself to [GitHub][github-url].

## Issues

See the [issue tracker][tracker-url].

[copr-url]: https://copr.fedorainfracloud.org/coprs/janbaudisch/git-mirror
[github-url]: https://github.com/janbaudisch/git-mirror
[tracker-url]: https://todo.sr.ht/~janbaudisch/git-mirror
