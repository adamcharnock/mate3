# Contributing

## General design decisions

- Keep it simple for now - both for developers and for users. Don't worry too much about weird edge cases that could arise, unless they're likely to occur (i.e. someone reports it).
- General Intellisense behaviour is important since we've got so many fields. And having a type annotation on them is even better for auto-completion etc. Since we're using dynamically generated models, it'd be tempting (and probably cleaner) to make liberal use of `__getattr__`, but we don't, 'cos that'd mess with Intellisense.
- Documentation and tests come when there's time/users. Tests are best for now, as they serve as documentation too.

## Brief overview of the code ...

The key things to note are:

- Stuff related to SunSpec should go in `./sunspec`.
- `./sunspec/models.py` includes the field definitions, and is auto-generated from `./sunspec/scripts/code_generator.py`.
- All the other code for reading/interacting then utilises these definitions.
- There are some basic tests - it'd be nice to have more!
- Using the caching options in `Mate3Client` or the CLI are best for developing, as it avoids bricking your device.

## Code contributions

If you wish to edit the mate3 source (contributions are gladly received!), then you can get the project directly from GitHub:

```sh
# Install poetry if you don't have it already (if you're unsure, you don't have it)
pip install poetry

# Get the source
git clone https://github.com/adamcharnock/mate3.git
cd mate3

# Install mate3 and its dependencies. This also makes the mate3 command available.
poetry install

# Run the tests - there aren't many, so feel free to add more!
pytest .
```

After this you should be able to run the `mate3` command and edit the project's source code.

## Release process

```sh
# Check everything has been comitted
git diff

# Up the version
poetry version {major|minor|bug}

# Update setup.py et al
dephell deps convert

# Review the resulting changes
git diff

# Build
poetry publish --build

# Docker: build & push
docker build -t adamcharnock/mate3:{VERSION_HERE} .
docker push adamcharnock/mate3:{VERSION_HERE}

# Commit
git ci  -m "Version bump"
git push
git push --tags
```