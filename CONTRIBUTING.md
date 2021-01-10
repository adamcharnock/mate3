# Contributing

## Brief overview of the code ...

The key things to note are:

- All the modbus information about devices/fields/etc. is auto-generated from `./sunspec/doc/OutBack.Power.SunSpec.Map.xlsx`. 
- All the other code for reading/interacting then utilises these definitions.
- If it seems weird that e.g. we have `Field`s and `FieldValue`s, this is why. The `Field` is the pure things parsed from the specification provided by Outback, which we want to keep clean and separate. The `FieldValue` is then the thing you actually interact with (and references an underlying `Field`). Maybe there's a nicer way of doing it, but for now this works.
- Typing is handy.
- General focus is on simple usage for the majority of use cases.
- There are some basic tests - it'd be nice to have more!
- Using the caching options in `Mate3Client` or the CLI are best for developing, as it avoids bricking your device.

## Code contributions

If you wish to edit the mate3 source (contributions are gladly received!), 
then you can get the project directly from GitHub:

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