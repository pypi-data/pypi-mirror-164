# linkedin-matrix

[![Lint, Build, and Deploy](https://github.com/beeper/linkedin/actions/workflows/deploy.yaml/badge.svg)](https://github.com/beeper/linkedin/actions/workflows/deploy.yaml)
[![Matrix Chat](https://img.shields.io/matrix/linkedin-matrix:nevarro.space?server_fqdn=matrix.nevarro.space)](https://matrix.to/#/#linkedin-matrix:nevarro.space?via=nevarro.space&via=sumnerevans.com)
[![Apache 2.0](https://img.shields.io/pypi/l/linkedin-matrix)](LICENSE)

LinkedIn Messaging <-> Matrix bridge built using
[mautrix-python](https://github.com/tulir/mautrix-python) and
[linkedin-messaging-api](https://github.com/sumnerevans/linkedin-messaging-api).

## Documentation

Not much yet :)

It is a Poetry project that requires Python 3.9+, PostgreSQL. Theoretically, all
you need to do is:

1. Copy the `linkedin_matrix/example-config.yaml` file and modify it to your
   needs.

2. Install the dependencies with Poetry:

   ```
   $ poetry install
   ```

   and activate the virtualenv.

3. Generate the registration file

   ```
   $ python -m linkedin_matrix -g
   ```

   and add it to your Synapse config.

4. Run the bridge using:

   ```
   $ python -m linkedin_matrix
   ```

### Features & Roadmap

[ROADMAP.md](ROADMAP.md) contains a general overview of what is supported by the
bridge.

## Discussion

Matrix room:
[`#linkedin-matrix:nevarro.space`](https://matrix.to/#/#linkedin-matrix:nevarro.space?via=nevarro.space&via=sumnerevans.com)
