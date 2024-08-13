# Use the official OCaml image
FROM ocaml/opam:ubuntu

# Set the working directory inside the container
WORKDIR /app

# Copy your project into the container
COPY . .

# Install dependencies (if any)
 RUN opam install . --deps-only

# Build your project (update this command based on your build system)
# RUN eval $(opam env) && dune build

# Command to run your application
# CMD [ "your_application_command_here" ]