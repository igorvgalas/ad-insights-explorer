import { StyleFunctionProps, extendTheme } from "@chakra-ui/react";
import { fonts } from "./fonts";

const theme = (color:string) =>
  extendTheme({
    colors: color,
    fonts: fonts,
    styles: {
      global: (props: StyleFunctionProps) => ({
        body: {
          color: props.colorMode === "light" ? "#000000" : "#FFFFFF",
        },
      }),
    },
  });

export default theme;
