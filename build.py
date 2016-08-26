from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="eliaskousk")
    builder.add_common_builds(shared_option_name="gtest:shared", pure_c=False)
    builder.run()

