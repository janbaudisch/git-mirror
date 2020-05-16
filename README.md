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

If you also want to use the `git-mirror-auto` script and Systemd timer, you also have to install these files using the same method.
Check your systems documentation on how to install Systemd files.

### Packages

I maintain a [copr repo][copr-url] for Fedora and CentOS.
To enable it and install the package run:

```
sudo dnf copr enable janbaudisch/git-mirror
sudo dnf install git-mirror
```

## Usage

For details, see the manual page for `git-mirror(1)` (and `git-mirror-auto(1)`) or `git-mirror help`.

There are two commands - `setup` and `update` - as well as a batch-update script along with a Systemd timer.

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

### `git-mirror-auto` and systemd

The `git-mirror-auto` script takes one directory to batch update all subdirectories using `git-mirror update`.
The directory to check is provided as a commandline argument or via the `UPDATE_DIRECTORY` environment variable.

There is also a Systemd timer provided: `git-mirror-auto.timer` (with the according service file).
It will run the `git-mirror-auto` script every 5 minutes.
To use this timer, set the directory to update in `/etc/git-mirror/git-mirror-auto.env` (default is `/var/git-mirror`) and enable the timer:

```
systemctl enable git-mirror-auto.timer
```

## Example Usage

### 1. Setup

Set up a new mirror directory.

```
git-mirror setup /var/git-mirror/some-mirror https://someserver.domain/user/tomirror git@someserver.domain/user/mirror
```

### 2. (a) Systemd

Enable the timer:

```
systemctl enable git-mirror-auto.timer
```

### 2. (b) One cronjob for everything

Add a cronjob (e.g. with `crontab -e`) containing the following:

```
*/5 * * * * git-mirror-auto /var/git-mirror
```

### 2. (c) One cronjob for each mirror

Add a cronjob (e.g. with `crontab -e`) containing the following for every mirror to update:

```
*/5 * * * * git-mirror update /var/git-mirror/some-mirror
```

This will update the mirror(s) every 5 minutes.

## In Action

This code mirrors itself to [GitHub][github-url].

## Issues

See the [issue tracker][tracker-url].

[copr-url]: https://copr.fedorainfracloud.org/coprs/janbaudisch/git-mirror
[github-url]: https://github.com/janbaudisch/git-mirror
[tracker-url]: https://todo.sr.ht/~janbaudisch/git-mirror
